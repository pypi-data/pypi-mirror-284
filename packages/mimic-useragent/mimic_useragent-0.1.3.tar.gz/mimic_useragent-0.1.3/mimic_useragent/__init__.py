# -*- coding: utf-8 -*-
"""
Allows to generate a random or fixed user agent according to a given *seed*.

Firefox only.
"""

import random


def mimic_user_agent(seed=None) -> str:
    """
    Returns 'user-agent' string.

    Args:
        seed : int or None (default).

    Returns:
        str : returns random user-agent strings.
    """

    OS_PLATFORM = {
        "win": (
            "Windows NT 6.1",  # Windows 7
            "Windows NT 6.2",  # Windows 8
            "Windows NT 6.3",  # Windows 8.1
            "Windows NT 10.0",  # Windows 10
        ),
        "linux": (
            "X11; Linux",
            "X11; Ubuntu; Linux",
        )
    }
    OS_CPU = {
        "win": (
            "x86",  # 32bit
            "Win64; x64",  # 64bit
            "WOW64",  # 32bit process on 64bit system
        ),
        "linux": (
            "i686",  # 32bit
            "x86_64",  # 64bit
            "i686 on x86_64",  # 32bit process on 64bit system
        )
    }

    random.seed(seed)

    # firefox versions 103 - 127
    version = float(random.randint(103, 127))
    USER_AGENT = 'Mozilla/5.0 (NONE; rv:%.1f) Gecko/20100101 Firefox/%.1f' % (
                version, version
            )

    os_plat = random.choice(list(OS_PLATFORM.keys()))
    os_choice = random.choice(OS_PLATFORM[os_plat])
    cpu = random.choice(OS_CPU[os_plat])

    if os_plat == "win":
        user_agent = USER_AGENT.replace(
                                        "NONE", f'{os_choice}; {cpu}'
                                        )
    else:
        user_agent = USER_AGENT.replace(
                                        "NONE", f'{os_choice}; {cpu}'
                                        )

    return user_agent
