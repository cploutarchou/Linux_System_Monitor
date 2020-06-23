def convert_kb_to_human(kilobytes):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string"""
    kilobytes = float(kilobytes) * 1024
    kb = float(1024)
    mb = float(kb ** 2)  # 1,048,576
    gb = float(kb ** 3)  # 1,073,741,824
    tb = float(kb ** 4)  # 1,099,511,627,776

    if kilobytes < kb:
        return '{0} {1}'.format(kilobytes, 'Bytes' if 0 == kilobytes > 1 else 'Byte')
    elif kb <= kilobytes < mb:
        return '{0:.2f} KB'.format(kilobytes / kb)
    elif mb <= kilobytes < gb:
        return '{0:.2f} MB'.format(kilobytes / mb)
    elif gb <= kilobytes < tb:
        return '{0:.2f} GB'.format(kilobytes / gb)
    elif tb <= kilobytes:
        return '{0:.2f} TB'.format(kilobytes / tb)
