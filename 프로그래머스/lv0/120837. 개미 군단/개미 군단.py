def solution(hp):
    general = hp//5
    soldier = (hp%5)//3
    worker = ((hp%5)%3)//1
    return general+soldier+worker
