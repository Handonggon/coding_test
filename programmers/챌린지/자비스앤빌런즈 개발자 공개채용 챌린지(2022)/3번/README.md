![Alt text](https://velog.velcdn.com/images%2Fjesahan%2Fpost%2Fd2c41950-b7ca-45fb-876c-59c7a3ca1f99%2Fimage.png)

## [문제]
#### [문제 설명]
<div class="challenge-markdown"><div class="markdown solarized-dark"><p>지뢰 찾기(Minesweeper)는 혼자서 하는 컴퓨터 게임입니다. 이 게임의 목적은 지뢰를 피해서 지뢰밭의 모든 단추를 여는 것입니다.<br>
게임의 규칙은 다음과 같습니다.</p>

<ul>
<li>게임 화면은 여러 개의 네모꼴 단추(격자)로 이루어진 “지뢰밭”으로 이루어져 있습니다.</li>
<li>각 단추는 눌러서(클릭) 열 수 있습니다.</li>
<li>지뢰가 숨겨져 있는 단추를 눌러 열면 게임 오버(game over)가 됩니다.

<ul>
<li>이때, 숨겨져 있던 모든 지뢰의 위치가 화면에 표시됩니다.</li>
</ul></li>
<li>지뢰가 없는 단추를 열면, 열린 단추에 맞닿은 둘레(정북,북동,정동,남동,정남,남서,정서,북서)의 다른 단추에 숨겨져 있는 지뢰 개수가 나타납니다.

<ul>
<li>나타나는 숫자가 1 이상이라면 그 단추 하나만 열리게 됩니다.</li>
<li>만약 열린 단추와 맞닿아 있는 8개의 다른 단추에 지뢰가 없다면, 열린 단추는 활성화된 채 빈 단추로 남게 되며, 인접해 있는 8개의 단추 중에서 아직 열리지 않은 단추가 모두 연쇄적으로 열리게 됩니다.</li>
<li>연쇄적으로 열린 단추 또한 각 단추에 나타나는 숫자가 1 이상이라면 그 단추 하나만 열리게 되며, 빈 단추라면 다시 인접한 8개의 단추 중 아직 열리지 않은 모든 단추를 연쇄적으로 열고, 더 열리는 단추가 없을 때까지 이를 반복합니다.</li>
</ul></li>
</ul>

<p>예를 들어서 다음과 같이 가로 길이가 3이고 세로 길이가 3인 지뢰밭이 있다고 가정 하겠습니다. <br>
<img src="https://i.imgur.com/0Sc0FsZ.png" title="" alt="Imgur"></p>

<p>이 지뢰 밭에서 사용자가 (2, 2)를 클릭하게 되면 화면이 다음과 같이 바뀌게 됩니다. (사용자가 보는 화면에는 지뢰가 표시되지 않으나, 편의상 표시)<br>
<img src="https://i.imgur.com/hBrvZAk.png" title="" alt="Imgur"></p>

<p>다른 예로 다음과 같이 가로 길이가 9이고 세로 길이가 9인 지뢰밭이 있다고 가정 하겠습니다.<br>
<img src="https://i.imgur.com/6Ry3Xsw.png" title="" alt="Imgur"></p>

<p>이 지뢰밭에서 사용자가 (0, 0)을 클릭하게 되면 사용자가 보는 화면은 다음과 같이 바뀌게 됩니다.<br>
<img src="https://i.imgur.com/WhBB7XO.png" title="" alt="Imgur"></p>

<p>처음 지뢰밭의 상태 board와 사용자가 클릭한 위치 y, x 가 매개변수로 주어질 때, (y, x) 를 눌렀을 때 사용자가 보게되는 지뢰밭의 상태를 return하는 solution 함수를 완성해 주세요.</p>

#### [제한 조건]
<li>지뢰밭은 'M'과 'E'로만 이루어진 문자열 배열로 주어집니다.</li>
<li>지뢰의 위치는 'M' 으로 표시됩니다.</li>
<li>지뢰가 없는 위치는 'E' 로 표시됩니다.</li>
<li>지뢰밭의 가로, 세로 크기는 최소 3, 최대 50이며, 항상 직사각형 모양입니다.</li>
<li>사용자가 열게 되는 단추의 위치 ( y, x )가 지뢰밭을 벗어나는 경우는 없습니다.</li>
<li>y는 세로축 좌표, x는 가로축 좌표를 나타냅니다.</li>
<li>return 하는 형식은 다음을 참고해주세요.

<li>만약 바로 지뢰를 누를 경우에는 누른 지뢰를 'X'로 표시하고, 나머지 지뢰는 모두 'M'으로 표시해서 return 해주세요.</li>
<li>지뢰밭에서 숫자는 인접한 8칸(정북, 북동, 정동, 남동, 정남, 남서, 정서, 북서)에 존재하는 지뢰의 수를 의미합니다.</li>
<li>지뢰밭에서 활성화된 빈 단추는 'B'로 표시합니다.</li>
<li>사용자가 지뢰가 없는 단추를 열 경우, 열려야 하는 모든 단추에 적절한 값을 채운 후, 지뢰가 있는 단추와 아직 열리지 않은 단추는 모두 'E'로 채워서 문자열 배열형태로 return 해주세요.</li>

#### [입출력 예]
<table class="table">
        <thead><tr>
<th>board</th>
<th>y</th>
<th>x</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>["EEEEE","EEMEE","EEEEE", "EEEEE"]</code></td>
<td>2</td>
<td>0</td>
<td><code>["B1E1B","B1E1B","B111B","BBBBB"]</code></td>
</tr>
<tr>
<td><code>["MME","EEE","EME"]</code></td>
<td>0</td>
<td>0</td>
<td><code>["XME", "EEE", "EME"]</code></td>
</tr>
</tbody>

## [입출력 예 설명]
<p>입출력 예시 #1<br>
초기 지뢰 밭의 상태는 다음과 같습니다.<br>
<img src="https://i.imgur.com/vSNsB81.png" title="" alt="Imgur"><br>
(2, 0)을 누르게 되면 다음과 같이 바뀌게 됩니다.<br>
<img src="https://i.imgur.com/LMKKwGp.png" title="" alt="Imgur"></p>

<p>입출력 예시 #2<br>
초기 지뢰 밭의 상태는 다음과 같습니다.<br>
<img src="https://i.imgur.com/0Sc0FsZ.png" title="" alt="Imgur"><br>
(0, 0)을 누르게 되면 지뢰 이므로 <code>X</code>로 바뀌게 되고, 남은 지뢰의 위치가 나오게 됩니다.<br>
<img src="https://i.imgur.com/KKbwxjc.png" title="" alt="Imgur"></p>
</div></div></div>
