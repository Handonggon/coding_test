#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int n_max = 10000;
int chains[n_max] = {1};
int min_chains[n_max];

bool addition_chains(int n, int candidate, int nr_chains, int& min_nr_chains, int chains[])
{
	int i;
	if (binary_search(chains, chains + nr_chains, n - candidate)) {
		if (nr_chains < min_nr_chains) {
			min_nr_chains = nr_chains;
			memcpy(min_chains, chains, sizeof(int) * min_nr_chains);
		}
		return true;
	}
	else if (nr_chains + 1 < min_nr_chains) {
		i = nr_chains - 1;
		for ( ; i >= 0; i--) {
			int s = candidate + chains[i];
			if (s < n) {
				chains[nr_chains] = s;
				if (!addition_chains(n, s, nr_chains + 1, min_nr_chains, chains))
					break;
			}
		}
		return (i == nr_chains - 1) ? false : true;
	}
	else {
		return false;
	}
}

int main()
{
	while (true) {
		int n;
		cin >> n;
		if (!n)
			break;
		int min_nr_chains = n;
		if (n > 1) {
			addition_chains(n, chains[0], 1, min_nr_chains, chains);
			for (int i = 0; i < min_nr_chains; i++)
				cout << min_chains[i] << ' ';
		}
		cout << n << endl;
	}
	return 0;
}