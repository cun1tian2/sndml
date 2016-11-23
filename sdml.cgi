#!/usr/local/bin/perl --
#----sdml.cgi----(161108 renewal old_smtp.cgi_xrehan)
# Synopsys .../sdml.cgi?totab=&to=hoge@bar.com&bcc=&frm=&sbj=&bdy=
#  name=totabはselect-opt入力操作上のﾀﾞﾐｰ、
#  直接アクセスは http://....cgi?&to=hoge@bar.com のみ且つHtmlEntityNoEncodingで送信可。
#  結果出力 (httpｽﾃｰﾀｽｺｰﾄﾞSent|cantOpen|no-rcpnt) mm/dd hh:mm 入力ﾌｫｰﾑ。

$adrslst1=' hana@k1.xrea.com ss292@s292.xrea.com tmrkti@gmail.com tmr445tmr445tmr@docomo.ne.jp';
$adrslst2=' hana@k1.xrea.com s89335@s335.xrea.com tmrkti@gmail.com hoge@foo.bar.com';

$sendmail="/usr/sbin/sendmail";
use HTML::Entities; # encode_entities( $str,q( <&>'") ); # unsafe_chars q(<&>'")、q(..)に半角SPも入れる
use CGI
$cgi=CGI->new();
($itself)=($0=~/([^\/]+)$/);
$to=$cgi->param("to");
$bcc=$cgi->param("bcc");
$rcpt="$to $bcc";
$rcpt=~s/[,; ]+/ /g;
$frm=($cgi->param("frm") || '');
 $adrslst2=$frm.$adrslst2;
$sbj=$cgi->param("sbj");	$sbjenc=encode_entities( $sbj, q(<&>'") );
$bdy=$cgi->param("bdy");	$bdyenc=encode_entities( $bdy, q(<&>'") );

if($to || $bcc){	# $to || $bcc
   if ($rslt=open MAIL,"|$sendmail $rcpt"){
	print MAIL "To:$to\nBcc:$bcc\nFrom:$frm\n","Subject:$sbj\n\n","$bdy";
	close MAIL;
	$rslt.="Sent ";
   }
   else{$rslt="cantOpen sendmail"}
}
else{$rslt="no-rcpnt ";}

# Shift_JIS 要fileSave and <meta http-equiv=content-type content=charset=UTF-8> on xrehbr UTF-8では不可
print <<ETX;
Content-Type: text/html\n\n<html>
<meta http-equiv=content-type content=charset=utf-8>
$rslt@{[sprintf "%d/%d %02d:%02d",(localtime)[4]+1,(localtime)[3,2,1]]}
<script type=text/javascript><!--
arry1="$adrslst1".split(" "); arry2="$adrslst2".split(" ");
document.write("<form name=form1 action=$itself>");
document.write("<select name=totab size=1 onchange=autoinp()>");	optwrt(arry1);
document.write("</select>↓<br>to:<input type=text name=to size=25 value=$to>");
document.write("<br>bcc<input type=text name=bcc value=$bcc>");
document.write("<br>frm<select name=frm size=1>");	optwrt(arry2);
document.write("</select><br>sbj<input type=text name=sbj size=25 value=\'$sbjenc\'>");
document.write("<br>bdy<input type=text name=bdy size=25 value=\'$bdyenc\'><br><input type=submit></form></html>");
fcs(form1.to);			 // オブジェクト[document.]form1.cmdlのdocument部省略可
//----------------------------------------------
function optwrt(arry){
	for(i in arry){document.write("<option value="+arry[i]+">"+arry[i]+"</option>");}
}
function fcs(arg){arg.focus(); } // 引数渡しは親オブジェクトが必要、子のみは不可
function autoinp(){
	slct=document.form1.totab.value; to=document.form1.to.value;	// slct,to変数宣言
	if(slct==""){ to=""; }
	else	    { to=(to) ? to + "," + slct : slct; }		// 3項演算子 (式)?yy:zz;
	form1.to.value=to
	fcs(form1.to);
}
//--></script>
ETX
__END__

=pod
161123 print <<ETX;の中に '# 無名sub @{...}  "mm/dd hh:mm"' があるとsntxErr→取除く。
       $rslt@{[sprintf... ]} 構文不可解？
161119 html://xxx/sdml.cgi?to=hoge@foo.bar.com MaiHeder_to:のみ且つHtmlEntityNoEncodeでも送信可。
       c-value=\'$sbjenc\'>" 半角spが入ると以降form入力ｴﾘｱに復元表示しない、半角spがあるとそこで値の終了とみなされ、要$value=''括弧で括る       
161111 c- Encode(ﾒｰﾙsbj,bdyｴﾝｺｰﾄﾞ、HTML::Entities(入力ｴﾘｱ復元
       c- arry2($adrslst2)の頭の[sp]部にfromｸｴﾘを戻す(select option
161111 x- ﾔﾒ select name=totab不要、sub-autoinp有り除去不可
161108 xre..*smtp.cgi renewal to sdml.cgi
  DVD F:\110602bkupNecWxp(1.3G\Documents and Settings\t\デスクトップ\作業中cgi\cbからコピー。
110320(add "," rcpt bcc),1103xxcreate    simpl_sendmail

  print `perl -cw xx.cgi 2>&1`;
  print `perl -MO=Deparse xx.cgi 2>&1`;
  Perl真っ先に覚えたいモジュール https://bayashi.net/diary/2013/0415
  Data::Dumper,YAML	Test::More	note explain $ref;	Devel::Peek	B::Deparse
  デバッガ(perl -d foo.pl、$ perldoc perldebug)		
 ●HTML::Entities - HTMLエンティティ(実体参照)文字列をエンコード/デコード http://perldoc.jp/docs/modules/HTML-Entities-3.55/Entities.pod ﾕﾆｺｰﾄﾞ等ﾏﾙﾁﾊﾞｲﾄ文字とhtmlｴﾝﾃｨﾃｨを含む文字列をhtmlｴﾝﾃｨﾃｨのみエンコードする法
ｴﾝｺｰﾄﾞされる規定値の文字セットはコントロール文字、8ビット目が設定の文字、 <&>'" の5つが規定値でエクスポートされる
encode_entities( $string, $unsafe_chars ); # $unsafe_charsを q( <&>'" ) 等で指定する(省略ではutf8ｺｰﾄﾞが化ける).
=cut
