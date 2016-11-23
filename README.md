# sndml
re-create sndml.cgi
161123 sdml.cgi update all, print <<ETX;の中の'# 無名sub @{...}  "mm/dd hh:mm"' が存在しsntxErr→取除く。
       更に $rslt@{[sprintf... ]} の構文不可解？ rslt内容とと日付をhtml内に？書き出したもの
       @{[sprintf "%d/%d %02d:%02d",(localtime)[4]+1,(localtime)[3,2,1]]} は日付の配列リスト？
       
       
