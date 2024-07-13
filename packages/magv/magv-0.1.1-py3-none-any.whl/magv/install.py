import os

def install(path, config):
    if not os.getuid() == 0:
        config.logger.warning("WARNING: You are trying to install an extension without sudo")
    try:
        os.chdir(path)
        if os.path.isfile("autogen.sh"):
            if not os.system("sh ./autogen.sh") == 0:
                config.logger.error("An error occured when running autogen.sh")
                raise Exception
        if os.path.isfile("configure"):
            if not os.system("./configure") == 0:
                config.logger.error("An error occured when running configure")
                raise Exception
        if not os.system("make") == 0:
            config.logger.error("An error occured when running making")
            raise Exception
        if not os.system("make install") == 0:
            config.logger.error("An error occured when running making install")
            raise Exception
    except Exception as e:
        config.logger.error("Installation failed")