'''
국, 영, 수 과목의 점수를 입력받아서
평균 점수를 통해 A ~ F 학점을 출력하시오.
'''

class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math  # ()가 없는 self 는 속성(프로퍼티)

    def avg(self):
        return self.sum() / 3  # ()로 되어있는 self 는 메소드

    def get_grade(self):
        score = int(self.avg())

        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        elif score >= 50:
            grade = 'E'
        else:
            grade = 'F'

        return grade

    @staticmethod
    def main():
        while 1:
            menu = input('0-종료 1-학점\n')
            if menu == '0':
                break
            elif menu == '1':
                kor = int(input('국어 점수 : '))
                eng = int(input('영어 점수 : '))
                math = int(input('수학 점수 : '))
                grade = Grade(kor, eng, math)
                print(f' 국어 {grade.kor}점, 영어 {grade.eng}점, 수학 {grade.math}점 :: 학점은 {grade.get_grade()}')
            else:
                input('메뉴선택 오류')


Grade.main();
