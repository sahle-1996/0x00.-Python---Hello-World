def print_python_list(p):
    size = len(p)
    alloc = sys.getsizeof(p)

    print("[*] Python list info")
    if not isinstance(p, list):
        print("  [ERROR] Invalid List Object")
        return

    print("[*] Size of the Python List = {}".format(size))
    print("[*] Allocated = {}".format(alloc))

    for i, item in enumerate(p):
        print("Element {}: {}".format(i, type(item).__name__))
        if isinstance(item, bytes):
            print_python_bytes(item)
        elif isinstance(item, float):
            print_python_float(item)

def print_python_bytes(p):
    size = len(p)

    print("[.] bytes object info")
    if not isinstance(p, bytes):
        print("  [ERROR] Invalid Bytes Object")
        return

    print("  size: {}".format(size))
    print("  trying string: {}".format(p.decode("utf-8", "replace")))

    truncated_bytes = p[:10] if size > 10 else p
    print("  first {} bytes: {}".format(len(truncated_bytes), " ".join(["{:02x}".format(b) for b in truncated_bytes])))

def print_python_float(p):
    print("[.] float object info")
    if not isinstance(p, float):
        print("  [ERROR] Invalid Float Object")
        return

    print("  value: {}".format(p))
