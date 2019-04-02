# Django Skeleton

This is a basic docker container and django application which can be used as a template, or skeleton, for new projects.

## Install and Run Docker

First, get docker for [mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac) or [windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows). Once your installation is complete, clone this repo and open the base directory in a terminal / PowerShell. Use the docker CLI to start a bash prompt in a new python container:

```
docker run --rm -v $(pwd):/opt/skeleton --workdir /opt/skeleton -it python:3.7.3 bash
```

## Your Assignment

This container is just standard python running on Debian Stretch. Document, using Markdown, the steps necessary to do the following things:

1. Install the python dependencies necessary to run the `skeleton` django application
1. Make a database **migration** for `skeleton` and activate the django application's database models by running **migrate**
1. Run the skeleton app's test suite successfully:
    ```
    python3 manage.py test
    ```

Write for a user who is a social scientist with some Python and data science experience but who is by no means a developer or Pythonista; the documentation you produce should explain in plain language what each command is actually doing. We don’t expect you to spend more than 90 minutes on this, so if you get stuck explain why and what you’d do with more time. Feel free to use existing documentation, walkthroughs, and other posts from anywhere on the Internet, but please list your sources at the bottom. Put your documentation in a GitHub gist and send us the link.

If you have questions, email [bbroderick@pewresearch.org](mailto:bbroderick@pewresearch.org).
