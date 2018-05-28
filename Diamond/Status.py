#
#   Copyright (c) 2018 Amit Green.  All rights reserved.
#
@gem('Diamond.Status')
def gem():
    require_gem('Diamond.Core')


    COUNT_MASK  = 0x0f
    STATUS_MASK = 0x30


    STATUS_ACTIVE   = 0x10
    STATUS_REMOVING = 0x20
    STATUS_ZAPPING  = 0x30


    status_map = {
        STATUS_ACTIVE   : "active",
        STATUS_REMOVING : "removing",
        STATUS_ZAPPING  : "zapping"
    }


    share(
        'COUNT_MASK',       COUNT_MASK,
        'STATUS_MASK',      STATUS_MASK,

        'STATUS_ACTIVE',    STATUS_ACTIVE,
        'STATUS_REMOVING',  STATUS_REMOVING,
        'STATUS_ZAPPING',   STATUS_ZAPPING,

        'status_map',       status_map,
    )
