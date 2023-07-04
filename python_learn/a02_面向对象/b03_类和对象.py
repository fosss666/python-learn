class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


c1 = Clock()
c1.id = 111
c1.price = 99
c1.ring()
