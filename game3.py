import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._hash_password(password)

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


def create_member():
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    return Member(name, username, password)


def create_post(author):
    title = input("게시물 제목을 입력하세요: ")
    content = input("게시물 내용을 입력하세요: ")
    return Post(title, content, author)


def main():
    members = []
    posts = []

    # 회원 인스턴스 생성
    for _ in range(3):
        member = create_member()
        members.append(member)

    # 회원 이름 출력
    print("회원 이름 목록:")
    for member in members:
        print(member.name)

    # 회원이 게시글 작성
    for member in members:
        for _ in range(3):
            post = create_post(member.username)
            posts.append(post)

    # 특정 유저가 작성한 게시글 제목 출력
    print("\n특정 유저가 작성한 게시글 제목:")
    for post in posts:
        if post.author == members[0].username:
            print(post.title)

    # 특정 단어가 포함된 게시글 제목 출력
    keyword = input("\n게시글 내용에 포함된 단어를 입력하세요: ")
    print(f"'{keyword}'가 포함된 게시글 제목:")
    for post in posts:
        if keyword in post.content:
            print(post.title)


if __name__ == "__main__":
    main()
