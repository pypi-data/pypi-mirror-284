# "That which does not kill us makes us stronger."
# ~ Friedrich Nietzsche


def install():
    from distutils.core import setup
    setup(name="data_structures",
          version="1.012",
          description="Python implementations of various data-sturctures",
          author="hero24",
          package_dir={'hero24/data_structures': '.'},
          packages=["hero24/data_structures"]
          )

if __name__ == "__main__":
    install()
