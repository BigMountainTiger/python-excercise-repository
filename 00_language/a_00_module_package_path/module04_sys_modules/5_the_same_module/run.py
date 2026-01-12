if __name__ == "__main__":
    
    import example_package.module_main as module_main
    import example_package.module_sub as module_sub
    import example_package

    # The same module is imported when it is imported directly and imported by a package __init__.py
    assert example_package.module_main is module_main
    assert example_package.module_sub is module_sub