import binascii
print(binascii.unhexlify("004D00610073007A0020006E006F0077006100200077006900610064006F006D006F007300630020004D004D00530020006F0064002000340038003800380034003100360037003700330033002E00200041006200790020006A00610020006F00620065006A0072007A006500630020007A0061006C006F00670075006A00200073006900650020006E0075006D006500720065006D002000740065006C00650066006F006E00750020006E0061002000680074007400700073003A002F002F006F00720061006E00670065002E0070006C002F006D006F006A002D006F00720061006E00670065002F006D006D007300200050006F007A006400720061007700690061006D0079002C0020004F00720061006E00670065").decode('utf-16-be'))