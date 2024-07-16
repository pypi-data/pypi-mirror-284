import os

def install(path, config):
    if os.getuid() == 0:
        print("WARNING: ")
        config.logger.warning("WARNING: You are trying to install an extension with sudo")
    try:
        if os.path.isfile(os.path.join(path, ".REQUIREMENTS")):
            with open(os.path.join(path, ".REQUIREMENTS")) as f:
                print("This extension requires the following libraries, please ensure you've already installed them: ")
                print(f.read())
                f.close()
                k = input("Proceed? (Y/n) ")
                if k == 'n' or k == 'N':
                    config.logger.info("User ends the installation because required libraries are not installed")
                    exit(0)
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