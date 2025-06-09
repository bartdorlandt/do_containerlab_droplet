# Digital Ocean Droplet with Containerlab and images

## Prerequisites
- A Digital Ocean account
- Have the API key in your environment variable as `DIGITALOCEAN_ACCESS_TOKEN`
- [task](https://taskfile.dev/installation/) installed on your local machine


# Images
By default, the latest nokia image is loaded into the local Docker registry. For adding additional images, follow the instructions below.

## Downloading images

Some tasks have been added to point you to the URLs where to get the images. Store them in the `docker_images` directory.

Like:

    task junos:download
    task arista:download

### Junos instructions

Once the file is downloaded run the convert command to prepare the docker image. This works on both AMD64 as well as ARM64 architectures.

    task junos:convert

### Arista instructions
Once the file is downloaded, `cEOS64` with the xz extension (only marked as such online). Once downloaded it is a `.tar` file. Have it placed in the `docker_images` folder and run the tar2targz command. This will convert all .tar files.

    task tar2targz


## docker_images folder

Any `.tar.gz` file in the `docker_images` folder will be loaded into the droplet and imported into the local Docker registry.

> Note: this is being pushed from your local machine to the droplet, so make sure you have enough bandwidth.

# End result
The end result is a Digital Ocean snapshot that contains the following:

* containerlab installed
* task installed
* the provided images preloaded into the local Docker registry

This can be used to create a new droplet allowing you to quickly spin up a new lab environment with the images you need.

# Next steps

With the snapshot created, you can now create a new droplet using the snapshot.

# Python scripts

The project uses `uv` to run the python scripts.

The purpose of the main scripts are:

* `create_droplet.py`
  * Creates a new droplet based on a snapshot of choice
* `shut_save_delete.py`
  * Shuts down the droplet, saves the state as a snapshot and deletes the droplet. With the idea of saving some money while not using the droplet.
    * Note: It will ask to delete the droplet. It is not mandatory to delete the droplet.

