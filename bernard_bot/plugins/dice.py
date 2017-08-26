from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import random


# @listen_to("!주사위 (\d*)?d?(\d+)?", re.IGNORECASE)
@listen_to("!roll ?(\d*d\d+.*)?", re.IGNORECASE)
def roll_dice(msg, roll_exp):
    # msg.reply("DEBUG MODE--")
    # msg.reply(roll_exp)

    if roll_exp is None:
        side_of_die = 6
        num_of_dice = 1
        modifier = "+ 0"

    else:
        captured = re.match("(\d*)?d(\d+) ?([+-] ?\d+)?", roll_exp, re.IGNORECASE)

        side_of_die = int(captured.group(2))

        num_of_dice = captured.group(1)
        if num_of_dice is '':
            num_of_dice = 1
        else:
            num_of_dice = int(num_of_dice)

        modifier = captured.group(3)
        if modifier is None:
            modifier = "+ 0"

    if num_of_dice > 100:
        msg.reply("주사위 갯수가 너무 많습니다! 조금 적게 굴려주세요~")
        return

    if num_of_dice == 0:
        msg.reply("은/는 주사위를 던졌다!")
        number_of_dice_error_messags = [
            "하지만 빈 손이었다...",
            "주사위가 없는데 던질수는 없다...",
            "공갈 주사위!",
            "아무것도 없는 주사위를 던진다는 것은 무엇인가. 봇은 고뇌에 빠지기 시작했다. 주사위가 던져지는 일은 없었다...",
        ]
        msg.reply(random.choice(number_of_dice_error_messags))
        return

    if side_of_die == 0:
        msg.reply("은/는 주사위를 던졌다!")
        die_error_messags = [
            "주사위는 0면체 주사위였기에 뒤틀린 황천으로 사라져버린거 같다...",
            "주사위가 손에서 빠져나오는 순간 디렉에 바다에 빠진거 같다...",
            "던지는 순간 눈부신 빛을 내며 주사위가 소멸했다. 물리적으로 존재할수 없는 주사위었던건가...",
            "주사위의 신의 목소리가 들려온다. `0면체는 던질 수 없다!`",
            "손을 펼쳐보았지만 빈 손바닥만 보인다.",
            "`하지만 무리에요. 0면체라니, 상상도 안간다구요 그런 주사위`, 주사위 봇은 시무룩해졌다..."
        ]
        msg.reply(random.choice(die_error_messags))
        return

    modifier_sign = modifier[0]
    modifier_number = int(modifier[1:].strip())

    # msg.reply(num_of_dice)
    # msg.reply(die)
    # msg.reply(modifier)
    # msg.reply(modifier_sign)
    # msg.reply(modifier_number)

    msg.reply("%d 면체를 %d 개 굴림 " % (side_of_die, num_of_dice))
    roll_result = [random.randrange(1, side_of_die, 1) for i in range(num_of_dice)]
    roll_sum = sum(roll_result)

    modified_result = roll_sum

    if modifier_sign == "+":
        modified_result += modifier_number
    elif modifier_sign == "-":
        modified_result -= modifier_number

    msg.reply("굴림: %s\n합계: %d, 평균: %.2f" % (roll_result, roll_sum, float(roll_sum) / float(len(roll_result))))
    if modifier_number != 0:
        msg.reply("수정치 적용: %d" % modified_result)


@listen_to("!rand ?(\d*)? .+", re.IGNORECASE)
def select_random_from_list(msg, n, l):
    if n is None or n == '' or int(n) <= 0:
        n = 1
    else:
        n = int(n)

    l2 = l.split("|")

    if n > len(l2):
        l3 = l2
    else:
        l3 = [i.strip() for i in random.sample(l2, n)]

    msg.reply("%s" % ", ".join(l3))


@respond_to("!rand help", re.IGNORECASE)
def rand_help(msg):
    msg.reply("""```
    주어진 목록에서 랜덤으로 몇개를 뽑아냅니다.
    !rand 1|2|3
    위의 예제는 1,2,3 중 하나를 골라서 돌려줍니다.
    !rand 4 1|2|3|5|6|7|8
    위의 예제는 1,2,3,4,5,6,7,8 중에서 4개를 골라서 돌려줍니다.
    
    편의상 예시는 숫자로 했지만 다음의 경우처럼 문자열도 가능합니다
    !rand 2 오징어|문어|고등어
    ```""")


@respond_to("!help", re.IGNORECASE)
def test_func(msg):
    msg.reply("주사위를 굴리는 법:")
    msg.reply("`!roll`")
    msg.reply("1d6을 굴립니다. 6면체 하나를 굴립니다.")
    msg.reply("1d6을 설명하면 다음과 같습니다. 6면체(d6)를 1개 굴린다.")
    msg.reply("3d20은 다음과 같습니다. 20면체(d20)를 3개 굴린다.")
    msg.reply("`!roll #d@` ex) `1d8`")
    msg.reply("#d@을 굴립니다. @면체 #개를 굴립니다.")
    msg.reply("`!roll #d@ + $`, ex) `1d12 + 5`")
    msg.reply("`!roll #d@ - $`, ex) `1d12 - 5`")
    msg.reply("#d@을 굴리고 수정치 $를 더하거나 뺍니다. @면체 #개를 굴립니다. 나온 결과의 합에 수정치 $를 더하거나 뺍니다.")
    msg.reply("A개의 B면체를 굴립니다.")
    msg.reply("수정치 M을 더하거나 뺍니다.")
