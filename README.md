# Metatrader Metrics

## About the Project

I created this project to enable the use of basic Metatrader metrics in Python. There are many possible calculations, but I think these are sufficient:

- RiskReward: This metric shows profitability (the number of trades does not impact the result).
- Z-Score: This measures the randomness of the strategy. It is different from the Z-score used in the tester. (https://www.mql5.com/en/articles/1492)
- Profit: The net profit.
- Trades: The number of trades, to ensure the comparison is valid in terms of trade volume.
- Buys/Sells: This shows whether the strategy is biased towards one side.
- Drawdown: If set to "abs," it calculates the drawdown in monetary value, else if you use Metatrader trade types and the type is not buy or sell, it will add the value to the capital and calculate the drawdown as a percentage of the capital.


## License

**Copyright 2024, kisb-data **  
kisbalazs.data@gmail.com 

## License

This code is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. If not, see <http://www.gnu.org/licenses/>.

### Additional Terms:

You may not use this software in products that are sold.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. **Redistributions of source code** must retain the above copyright notice, this list of conditions and the following disclaimer.

2. **Redistributions in binary form** must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

4. **Products that include this software may not be sold.**

## Warranty Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---