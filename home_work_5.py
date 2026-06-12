class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} + {self.earn()}"


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} + {self.viral()}"


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return f"{self.live()} + {self.viral()} + {self.earn()}"


glow = GlowStreamer()
viral = ViralCyborg()
donate = DonateMage()

print("GlowStreamer MRO:")
print(GlowStreamer.mro())
print(glow.live())
print("Сработал метод класса Streamer, потому что Streamer указан первым в наследовании.")
print(glow.ultimate_content())

print("ViralCyborg MRO:")
print(ViralCyborg.mro())
print(viral.live())
print("Сработал метод класса TikToker, потому что TikToker указан первым в наследовании.")
print(viral.ultimate_content())

print("DonateMage MRO:")
print(DonateMage.mro())
print(donate.live())
print("Сработал метод класса Streamer, потому что Streamer указан первым в наследовании.")
print(donate.ultimate_content())