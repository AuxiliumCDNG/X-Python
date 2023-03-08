alter = int(input("Wie alt bist du?"))

zu_jung = alter < 18
print(zu_jung)

if zu_jung:
    print("Zu jung")
if not zu_jung:
    print("Alt genug")


print("Test")

