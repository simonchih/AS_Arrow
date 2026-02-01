Card image source: PySol cardset
http://sourceforge.net/projects/pysolfc/?source=directory

Sound source (XiangQi Wizard):
https://sourceforge.net/projects/xqwizard/?source=directory

Game Name:
AS refer to Add and Subtract. During the game process, the card present as Arrow.

Game Rule:
Delete all card to win. User can drag and drop card from cards library to original
6 cards. At the game start, original 6 cards look like:

d
 b
e a
 c
f

User can connect d, e, f cards. Once d and e are deleted, user can connect to b.
It's similarly to c and a. Cards are positive for a, b, c, d, e, f. 
And then card is negative while connecting. In a similar way, 
the next card is positive (do the add), and then the card is negative (do the subtract).
The row of cards can be deleted as sum of cards pile is 0. 
But be carefully, if the number of cards is 12, but can't be deleted now, The game is over.
By the way, if cards library is empty and user can't win, the game is over.

Starting from v0.1.1, you can move an entire pile (except the first one) to another pile.
If the front half of a pile becomes 0 after applying +/?, you must click the pile of the next card in the back half (the one right after the 0) for the front half to be removed automatically.
If the original pile is cleared while you are dragging, releasing the drag will put the card into the deck.

Note: 
1. Click "NEW GAME!" can start a new game.
2. Click cheat image (NOT word), can ON/OFF cheat information. Cheat is ON by default.
But I suggest OFF, to play real AS Arrow.

Following README is for chinese:
遊戲名稱：AS Arrow
簡介：AS就是加(Add)和減(Subtract)，Arrow指的是，遊戲過程，看起來牌的形狀像箭頭。
這個遊戲是訓練玩家的加減法，和記憶力。

玩法：遊戲的目的，就是要消除所有的牌。這個遊戲的牌庫在左下角，
托曳牌庫的牌，可以接上去原本的牌。一開始的牌形是：

d
 b
e a
 c
f

只能接d, e, f 的牌，a, b, c, d, e, f 的牌是正(整數)的，再來接的牌是負的，
換句話說就是做相減的動作。之後再接的牌，是正的，也就是相加。
相加之後的牌又是相減，如此相加、相減，一直重複下去。
假如加或減起來的牌，一直到牌整列剛好是0，就可以整排牌消掉。
如果一開始的d跟e，都消除，
就可以開始接b的牌。同理，如果b跟c的牌都消除，就能接a的牌。
一但a列的牌都消除，就獲得最後的勝利。另外，如果一列牌達到12張，
還是不能消除，就會立刻結束遊戲。而牌庫抽牌抽完最後一張，還是未能取得勝利，
也會結束遊戲。

從v 0.1.1開始，可以移動除了第一張以外的整個牌列，到另一個牌列。
若是牌列中的某前半段加減後是0，
需點選加減後是0的下一張後半段的牌列，才會自動刪除前半段。
若是托曳中原本的牌列已經消除，此時停止托曳會把牌放入牌庫。

其它：
1. 按中間的NEW GAME!圖樣，可以重新開始遊戲
2. 按cheat開關的圖樣(非文字)，可以ON/OFF 提示的資訊，為了初學者方便，
預設是開的。不過關閉cheat，才是真正的AS Arrow.
3. J和K圖片的差別是，J戴全紅的帽子，Ｋ戴一條紅線，上面是黃色的帽子