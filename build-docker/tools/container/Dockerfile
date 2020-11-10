FROM gcc:8

#Set-up the versions and URL here
ARG VSCODE_BASEURL="https://github.com/microsoft/vscode/archive"
ARG VSCODE_VERSION="1.51.0"

#Start of image creation
ENV DEBIAN_FRONTEND=noninteractive

#Install necessary packages for the IDE
RUN apt update && apt install -y \
    dbus \
    git \
    libx11-dev \
    libx11-xcb-dev \
    libxcb-dri3-0 \
    libxcomposite-dev \
    libxcursor-dev \
    libxdamage-dev \
    libxi-dev \
    libxtst-dev \
    libnss3-dev \
    libatk1.0-dev \
    libatk-bridge2.0-dev \
    libgtk-3-dev \
    libxss-dev \
    libasound2-dev \
    libxkbfile-dev \
    libsecret-1-dev \
    && echo "Cleaning..." \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*


#Install Node.js (using nvm) and yarn (needed for the IDE)
ENV NODE_VERSION v12.19.0
ENV XDG_CONFIG_HOME="/software"
RUN mkdir /software \
    && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.0/install.sh | bash \
    && . /software/nvm/nvm.sh \
    && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION\
    && nvm use default

ENV NODE_PATH "/software/nvm/versions/node/$NODE_VERSION"
ENV PATH "$PATH:$NODE_PATH:$NODE_PATH/lib/node_modules"

#Install yarn
RUN mkdir -p /software/yarn \
    && curl -L https://yarnpkg.com/latest.tar.gz -o /software/tmp.tgz \
    && tar -xf /software/tmp.tgz -C /software/yarn --strip-components=1 \
    && rm /software/tmp.tgz

ENV PATH "$PATH:/software/yarn/bin"

#Start installation of a *specific* version of the IDE here
ENV VSCODE_URL "$VSCODE_BASEURL/$VSCODE_VERSION.tar.gz"
#Download and extract the IDE
RUN mkdir /software/ide \
    && curl -L $VSCODE_URL -o /software/ide/vscode.tgz \
    && tar -xf /software/ide/vscode.tgz -C /software/ide --strip-components=1 \
    && rm /software/ide/vscode.tgz

#Install the IDE by compiling
#Note use of bash -c, to ignore any exit-codes of underlying commands
RUN bash -c '. /software/nvm/nvm.sh; nvm use default; cd /software/ide;\
    yarn install; yarn run compile; yarn run electron'

#Copy execution script to /software directory (work-around for nodejs)
COPY ./launch-ide.sh /software/launch-ide.sh
RUN chmod +x /software/launch-ide.sh \
    && mkdir /build \
    && mkdir /src \
    && mkdir /var/run/dbus \
    && rm -rf /root/.cache \
    && rm -rf /usr/local/share/.cache

WORKDIR /src
