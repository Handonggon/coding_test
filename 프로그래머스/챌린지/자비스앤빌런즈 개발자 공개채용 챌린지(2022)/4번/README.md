![Alt text](https://velog.velcdn.com/images%2Fjesahan%2Fpost%2Fd2c41950-b7ca-45fb-876c-59c7a3ca1f99%2Fimage.png)

## [문제]
#### [문제 설명]
<div class="challenge-markdown"><div class="markdown solarized-dark"><p>1부터 n까지의 숫자가 시계방향으로 붙은 스택 n개가 각자의 bottom을 서로 공유하는 자료구조를 만들려 합니다. 이 때, 모든 스택이 서로 공유하는 가장 안쪽 공간을 "중앙 공간"이라고 합니다. 예를 들어, 다음 그림은 5개의 스택이 중앙을 공유하는 모습을 나타낸 것입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/f3088d2d-41b6-4e99-8c5e-c9ff7f4c695b/example1.png" title="" alt="example1.png"></p>

<p>위 그림에서 각 스택이 갖고 있는 원소는 다음과 같습니다.</p>

<ul>
<li><code>s1 = [1 / 7, 4]</code></li>
<li><code>s2 = [1 / 3, 6, 4, 9]</code></li>
<li><code>s3 = [1 / 12, 3, 11]</code></li>
<li><code>s4 = [1 / 4, 1]</code></li>
<li><code>s5 = [1 / 7, 3, 7]</code></li>
</ul>

<p>모든 스택이 1이라는 수를 중앙 공간에 공유하고 있기 때문에, <code>[1 / ..]</code> 라는 방식의 표기를 하였음에 유의하세요.</p>

<p>이 자료구조는 원소를 푸쉬(push)하고 팝(pop)하는 방식이 일반적인 스택과는 조금 다릅니다. 여기에서는 다음과 같은 방식으로 push 연산과 pop 연산을 정의합니다.</p>

<ul>
<li><code>push(i, x)</code> : i번 스택에 정수 x를 넣습니다. 만약 i번 스택을 포함한 모든 스택이 완전히 비어있다면, 중앙 공간에 x가 들어가게 됩니다.</li>
<li><code>pop(i)</code>: i번 스택의 가장 바깥에 있는 원소를 제거합니다. 

<ul>
<li>만약, 중앙 공간에 있던 수가 제거된다면, 중앙 공간을 제외한 다른 원소가 적어도 1개 이상 들어있는 스택 중 시계방향으로 가장 가까운 스택의 원소들이 중앙 공간 방향으로 한 칸씩 이동합니다.</li>
<li>만약 그런 스택이 없다면 아무 일도 하지 않습니다.</li>
</ul></li>
</ul>

<p>다음은 중앙을 공유하는 빈 스택 3개가 연결된 예시입니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/8ab33e6e-5821-490c-a622-df9d5caa16d2/example2.png" title="" alt="example2.png"></p>

<ul>
<li><code>s1 = []</code></li>
<li><code>s2 = []</code></li>
<li><code>s3 = []</code></li>
</ul>

<p>여기서 <code>push(1, 4)</code> 연산을 실행하면, 1번 스택에 4를 넣게 됩니다. 모든 스택이 비어있으므로, 이 4는 중앙 공간으로 들어갑니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/2b1f0b8c-3da2-4200-9b0f-089823fd1529/push_1_4.png" title="" alt="push_1_4.png"></p>

<ul>
<li><code>s1 = [4]</code></li>
<li><code>s2 = [4]</code></li>
<li><code>s3 = [4]</code></li>
</ul>

<p>그 다음에 <code>push(2, 2)</code> 연산을 실행하면, 2번 스택에 2를 넣게 됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/1c7439e6-ed56-4f1a-a8ed-8b882576d1b3/push_2_2.png" title="" alt="push_2_2.png"></p>

<ul>
<li><code>s1 = [4]</code></li>
<li><code>s2 = [4 / 2]</code></li>
<li><code>s3 = [4]</code></li>
</ul>

<p>그 다음에 <code>push(1, 3)</code> 연산을 실행하면, 1번 스택에 3을 넣게 됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/b11d94d7-5aa7-47c5-a48a-179d82e55af3/push_1_3.png" title="" alt="push_1_3.png"></p>

<ul>
<li><code>s1 = [4 / 3]</code></li>
<li><code>s2 = [4 / 2]</code></li>
<li><code>s3 = [4]</code></li>
</ul>

<p>그 다음에 <code>push(1, 6)</code> 연산을 실행하면, 1번 스택에 6을 넣게 됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/fe8cdfbd-a986-4a24-9d48-d29d17a5abe0/push_1_6.png" title="" alt="push_1_6.png"></p>

<ul>
<li><code>s1 = [4 / 3, 6]</code></li>
<li><code>s2 = [4 / 2]</code></li>
<li><code>s3 = [4]</code></li>
</ul>

<p>그 다음에 <code>pop(3)</code> 연산을 실행하면, 일반적인 스택에서의 pop 연산과 같이 3번 스택의 가장 바깥쪽에 있던 수인 4가 제거됩니다. 이 때, 중앙공간이 비게 되며, 중앙 공간 외에 다른 원소를 갖고있는 스택 중 3번 스택에서 시계방향으로 가장 가까운 1번 스택의 원소 [3, 6]이 한 칸씩 안쪽으로 이동합니다. 그 결과는 다음 그림과 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/1a1e44a6-b7fb-418f-8eb4-0c1f8fb10998/pop_3.png" title="" alt="pop_3.png"></p>

<ul>
<li><code>s1 = [3 / 6]</code></li>
<li><code>s2 = [3 / 2]</code></li>
<li><code>s3 = [3]</code></li>
<li>pop 연산으로 제거된 값 = 4</li>
</ul>

<p>그 다음에 <code>pop(2)</code> 연산을 실행하면, 2번 스택의 가장 바깥에 있던 원소인 2를 제거합니다. 이 때 2는 중앙 공간에 있던 수가 아니므로, 일반적인 스택에서의 pop 연산 외 다른 행동을 하지 않습니다. </p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/ybm/43ea3c0e-454a-4f08-8dc5-c3ae0c0b6f44/pop_2.png" title="" alt="pop_2.png"></p>

<ul>
<li><code>s1 = [3 / 6]</code></li>
<li><code>s2 = [3]</code></li>
<li><code>s3 = [3]</code></li>
<li>pop 연산으로 제거된 값 = 2</li>
</ul>

<p>스택의 개수 n과 실행할 연산의 목록을 나타내는 2차원 배열 queries가 매개변수로 주어집니다. 주어진 연산을 순서대로 실행하면서, pop 연산으로 제거된 숫자들을 차례대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.</p>

#### [제한 조건]
<ul>
<li>n은 2 이상 20 이하인 자연수입니다.</li>
<li>queries의 길이는 1 이상 1,000 이하입니다.

<ul>
<li>queries의 각 행은 <code>[a, b]</code> 형태입니다.</li>
<li>a는 1 이상 n 이하입니다.</li>
<li>b는 -1이거나 1 이상 1,000,000 이하입니다.</li>
<li>b가 1 이상이면, <code>push(a, b)</code> 연산을 실행한다는 의미입니다.</li>
<li>b가 -1이면, <code>pop(a)</code> 연산을 실행하고 제거된 값을 배열에 담으면 됩니다.</li>
<li>b가 -1인 행이 최소 1개 이상 있습니다.</li>
</ul></li>
</ul>

#### [입출력 예]
<table class="table">
        <thead><tr>
<th>n</th>
<th>queries</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td><code>[[1,4],[2,2],[1,3],[1,6],[3,-1],[2,-1]]</code></td>
<td><code>[4,2]</code></td>
</tr>
<tr>
<td>4</td>
<td><code>[[1,3],[1,2],[3,6],[3,-1],[4,5],[2,-1],[3,-1],[1,-1]]</code></td>
<td><code>[6,3,5,2]</code></td>
</tr>
<tr>
<td>5</td>
<td><code>[[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]</code></td>
<td><code>[-1,-1,-1,-1,-1]</code></td>
</tr>
</tbody>
      </table>

## [입출력 예 설명]
<p>입출력 예 #1</p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>실행할 연산을 순서대로 표현하면 다음과 같습니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>수행하는 함수</th>
<th>1번 스택</th>
<th>2번 스택</th>
<th>3번 스택</th>
<th>4번 스택</th>
<th>기타 사항</th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td>초기 상태</td>
</tr>
<tr>
<td><code>push(1, 3)</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td>중앙 지점에 3이 들어갑니다.</td>
</tr>
<tr>
<td><code>push(1, 2)</code></td>
<td><code>[3,2]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td>1번 스택에 2가 들어갑니다.</td>
</tr>
<tr>
<td><code>push(3, 6)</code></td>
<td><code>[3,2]</code></td>
<td><code>[3]</code></td>
<td><code>[3,6]</code></td>
<td><code>[3]</code></td>
<td>3번 스택에 6이 들어갑니다.</td>
</tr>
<tr>
<td><code>pop(3)</code></td>
<td><code>[3,2]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td>3번 스택에서 6을 제거합니다.</td>
</tr>
<tr>
<td><code>push(4, 5)</code></td>
<td><code>[3,2]</code></td>
<td><code>[3]</code></td>
<td><code>[3]</code></td>
<td><code>[3,5]</code></td>
<td>4번 스택에 5가 들어갑니다.</td>
</tr>
<tr>
<td><code>pop(2)</code></td>
<td><code>[5,2]</code></td>
<td><code>[5]</code></td>
<td><code>[5]</code></td>
<td><code>[5]</code></td>
<td>2번 스택에서 중앙 지점의 3을 제거하고, 4번 스택이 한 칸씩 안쪽으로 이동합니다.</td>
</tr>
<tr>
<td><code>pop(3)</code></td>
<td><code>[2]</code></td>
<td><code>[2]</code></td>
<td><code>[2]</code></td>
<td><code>[2]</code></td>
<td>3번 스택에서 중앙 지점의 5를 제거하고, 1번 스택이 한 칸씩 안쪽으로 이동합니다.</td>
</tr>
<tr>
<td><code>pop(1)</code></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td><code>[]</code></td>
<td>1번 스택에서 중앙 지점의 2을 제거하고, 모든 공간이 완전히 비어있게 됩니다.</td>
</tr>
</tbody>
      </table>
<ul>
<li>따라서, <code>[6,3,5,2]</code>를 return 해야 합니다.</li>
</ul>

<p>입출력 예 #3</p>

<ul>
<li>스택이 비어있는 상태에서 push를 하지 않고 계속 pop 연산만 했으므로, <code>[-1,-1,-1,-1,-1]</code>을 return 해야 합니다.</li>
</ul>
