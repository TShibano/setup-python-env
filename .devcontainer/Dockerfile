# Ref: https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
# pythonイメージを使用
FROM python:3.13-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates git   

# Setting User >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user
ARG USER_NAME
# UID/GIDはdevcontainerが自動で合わせてくれるので、コンテナOS内で被らないUID/GIDを指定する
ARG USER_UID=12345
ARG USER_GID=$USER_UID
ENV USER_NAME=${USER_NAME}
ENV USER_UID=${USER_UID}
ENV USER_GID=${USER_GID}
RUN groupadd -g ${USER_GID} ${USER_NAME} \
    && useradd -u ${USER_UID} -g ${USER_GID} -m ${USER_NAME} -s /bin/bash
USER ${USER_NAME}
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Setting User >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Download the latest installer
USER root
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN chmod a+x /uv-installer.sh && chown $USER_NAME:$USER_NAME /uv-installer.sh
USER ${USER_NAME}
# Run the installer
RUN sh /uv-installer.sh

# パスを通す
ENV PATH="/${USER_NAME}/.local/bin/:$PATH"
# remove the installer
USER root
RUN rm /uv-installer.sh
USER ${USER_NAME}
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
