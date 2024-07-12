import pkg_resources    



def get_current_vesion():
        library_name = 'therix'
        version = pkg_resources.get_distribution(library_name).version
        return version