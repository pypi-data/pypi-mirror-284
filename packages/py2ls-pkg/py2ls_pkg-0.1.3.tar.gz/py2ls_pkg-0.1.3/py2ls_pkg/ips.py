import subprocess
import sys


try:
    import pkg_resources
except ImportError:
    print("pkg_resources not found. Installing setuptools...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
    import pkg_resources

def upgrade_pip(): # Upgrade pip
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        print("Upgrading 'pip'...")
        print("'pip' upgrade successful.")
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading 'pip': {e}")


def install(package):
    """
    Install a package if not already installed.
    
    Parameters:
    package (str or list): Package name or list of package names to install.
    """
    if isinstance(package, list):
        for pkg_ in package:
            pkg.install(pkg_)
    try:
        import pkg_resources
        # Check if the package is available
        if package not in {pkg_.key for pkg_ in pkg_resources.working_set}:
            print(f"{package} not found. Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return True
        else:
            print(f"{package} is already installed.")
            return True
    except Exception as e:
        print(f"Failed to ensure {package} is installed. Reason: {e}")
        return False


def uninstall(keep=None, verbose=True):
    """
    Uninstall unwanted packages from the Python environment, keeping essential ones if specified.
    
    Parameters:
    keep (list or None): List of package names to keep. If None, keep essential packages.
    verbose (bool): If True, print uninstallation messages. Default is True.
    """
    # 重要的pkg
    keep_anyway = ['numpy', 'pandas', 'seaborn', 'ipykernel', 'pip', 'setuptools', 'pkg_resources',
                    'pytz','appnope','asttokens','certifi','comm','debugpy','decorator','executing',
                    'ipython','jedi','jupyter_client','jupyter_core','matplotlib-inline','nest-asyncio',
                    'packaging','parso','pexpect','pip','platformdirs','prompt_toolkit',
                    'psutil','ptyprocess','pure-eval','Pygments','python-dateutil','pyzmq',
                    'six','stack-data','tornado','traitlets','wcwidth']

    # Convert keep to a list if it's a string
    if isinstance(keep, str):
        keep = [keep]

    if keep is None:
        keep = keep_anyway
    else:
        keep.extend(keep_anyway)

    try:
        import pkg_resources
        installed_packages = {pkg_.key for pkg_ in pkg_resources.working_set} 
        packages_to_remove = installed_packages - set(keep)
        if verbose:
            print(f'\nPackages to keep: \n{keep}')
            print(f'\nPackages to remove: \n{packages_to_remove}')

        # Uninstall packages
        for package in packages_to_remove:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])
                if verbose:
                    print(f'\nSuccessfully uninstalled {package}')
            except Exception as e:
                if verbose:
                    print(f'\nFailed to uninstall {package}. \nReason: {e}')
    except Exception as e:
        print(f'Error: {e}')


def uninstall_except(keep=None, verbose=True):
    """
    Uninstall unwanted packages from the Python environment, keeping essential ones if specified.
    
    Parameters:
    keep (list or None): List of package names to keep. If None, keep essential packages.
    verbose (bool): If True, print uninstallation messages. Default is True.
    """
    # 重要的pkg
    keep_anyway = ['numpy', 'pandas', 'seaborn', 'ipykernel', 'pip', 'setuptools', 'pkg_resources']

    # Convert keep to a list if it's a string
    if isinstance(keep, str):
        keep = [keep]

    if keep is None:
        keep = keep_anyway
    else:
        keep.extend(keep_anyway)

    try:
        import pkg_resources
        installed_packages = {pkg_.key for pkg_ in pkg_resources.working_set} 
        packages_to_remove = installed_packages - set(keep)
        if verbose:
            print(f'\nPackages to keep: \n{keep}')
            print(f'\nPackages to remove: \n{packages_to_remove}')

        # Uninstall packages
        for package in packages_to_remove:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])
                if verbose:
                    print(f'\nSuccessfully uninstalled {package}')
            except Exception as e:
                if verbose:
                    print(f'\nFailed to uninstall {package}. \nReason: {e}')
    except Exception as e:
        print(f'Error: {e}')

upgrade_pip()

def main():
    upgrade_pip()

if __name__ == "__main__":
    main()

