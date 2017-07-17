from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="dario-ramos", channel="stable")
    builder.add_common_builds(shared_option_name="conan_boost:shared")
    builder.run()
