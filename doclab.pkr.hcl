packer {
  required_plugins {
    digitalocean = {
      version = ">= 1.4.1"
      source  = "github.com/digitalocean/digitalocean"
    }
  }
}

variable "do_token" {
  type    = string
  default = env("DIGITALOCEAN_ACCESS_TOKEN")
}

variable "region" {
  type    = string
  default = "ams3"
}

variable "size" {
  type    = string
  default = "s-1vcpu-1gb"
  # size         = "s-4vcpu-16gb-amd"
}

variable "image" {
  type    = string
  default = "ubuntu-24-04-x64"
}

source "digitalocean" "clab" {
  api_token     = var.do_token
  image         = var.image
  region        = var.region
  size          = var.size
  ssh_username  = "root"
  snapshot_name = "clab-devenv-${formatdate("YYYY_MM_DD, hh:mm", timestamp())}"
  tags          = ["clab"]
  snapshot_tags = ["clab"]
}

build {
  name    = "clab-devenv"
  sources = ["source.digitalocean.clab"]

  # Will need to change this to be the clab image files
  provisioner "file" {
    # This local directory must exist. mkdir -p docker_images
    source      = "./docker_images"
    destination = "/root/docker_images/"
  }

  provisioner "shell" {
    script = "scripts/install.sh"
  }

  provisioner "shell" {
    script = "scripts/containerlab.sh"
  }

  provisioner "shell" {
    script = "scripts/post.sh"
  }
}

