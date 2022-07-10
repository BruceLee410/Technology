def solution(skill, skill_trees):
    answer=0
    for tree in skill_trees: #tree는 스킬트리 원소
        tree_index = 0
        for char in tree: #char는 스킬트리 원소의 글자
            if char in skill: #스킬에 그 글자가 있다면
                if skill.index(char) > tree_index: #그 글자가 트리 인덱스보다 인덱스위치가 크다면
                    break                    #순서가 맞지 않으므로 나간다. 다음 트리 인덱스를 탐색함.
                elif skill.index(char) == tree_index:#그 글자가 트리인덱스와 인덱스위치가 같다면
                    tree_index += 1               #해당 tree원소 안에서 다시 다음 글자를 비교함
        else: 
            answer += 1     #대소 비교후 break안일어 나면 정답에 추가함.
    return answer
    #이중 포문을 써야하나
    #시간복잡도를 줄일 수 있는 방법이 있다.