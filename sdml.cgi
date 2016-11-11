#!/usr/local/bin/perl --
#----sdml.cgi----(161108 renewal old_smtp.cgi_xrehan)
#161111 c- Encode(ﾒｰﾙsbj,bdyｴﾝｺｰﾄﾞ、HTML::Entities(入力ｴﾘｱ復元
#       c- arry2($adrslst2)の頭の[sp]部にfromｸｴﾘを戻す(select option
#161111 x- ﾔﾒ select name=totab不要、sub-autoinp有り除去不可

$adrslst1=' hana@k1.xrea.com ss292@s292.xrea.com tmrkti@gmail.com tmr445tmr445tmr@docomo.ne.jp';
$adrslst2=' hana@k1.xrea.com s89335@s335.xrea.com tmrkti@gmail.com hoge@foo.bar.com';

$sendmail="/usr/sbin/sendmail";
use HTML::Entities;
use Encode;
use CGI
$cgi=CGI->new();
($itself)=($0=~/([^\/]+)$/);
$to=$cgi->param("to");
$bcc=$cgi->param("bcc");
$rcpt="$to $bcc";
$rcpt=~s/[,; ]+/ /g;
$frm=encode_entities( ($cgi->param("frm") || '') );
 $adrslst2=$frm.$adrslst2;
$sbj=encode_entities( $cgi->param("sbj") );	$sbjenc=Encode::encode('utf-8',$sbj);
$bdy=encode_entities( $cgi->param("bdy") );	$bdyenc=Encode::encode('utf-8',$bdy);
if($to || $bcc){	# $to || $bcc
   if ($rslt=open MAIL,"|$sendmail $rcpt"){
	print MAIL "To:$to\nBcc:$bcc\nFrom:$frm\n",
	"Subject:$sbjenc\n\n","$bdyenc";
	close MAIL;
	$rslt.="Sent ";
   }
   else{$rslt.="cantOpen sendmail"}
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
document.write("</select>↓<br>to:<input type=text name=to size=30 value=$to>");
document.write("<br>bcc<input type=text name=bcc value=$bcc>");
document.write("<br>frm<select name=frm size=1>");	optwrt(arry2);
document.write("</select><br>sbj<input type=text name=sbj size=30 value=$sbj>");
document.write("<br>bdy<input type=text name=bdy size=30 value=$bdy><br><input type=submit></form></html>");
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
161108 xre..*smtp.cgi renewal to sdml.cgi
#DVD F:\110602bkupNecWxp(1.3G\Documents and Settings\t\デスクトップ\作業中cgi\cbから# 110320(add "," rcpt bcc),1103xxcreate    simpl_sendmail
# revupPlan(htac.cgi?htatp=smtp.cgi?xxx id:pw cookie chk(操作性?)、<name>hoge@foo.bar.com可能化)
# symlink smtp.cgi -> sendmail.cgi ＆ smtpad(addrsFile)
# adrsFileでhistory.go(-1)使用不可、cgiに戻ると前のform入力画面で再実行されるため。
# sbj:日本語noEncodeのままで、docomo携帯受信日本語表示可、xrea受信日本語表示不可。
# 161108 11:08 c-cmntline c-charset=utf-8 (<meta charset="UTF-8">でも可)  5:00 c-$adrslst1/2 c-$sendmail c-TerapadTextEncodingUTF-8N
#  print `perl -cw xx.cgi 2>&1`;
#  print `perl -MO=Deparse xx.cgi 2>&1`;

#  Perl真っ先に覚えたいモジュール https://bayashi.net/diary/2013/0415
Data::Dumper,YAML	Test::More	note explain $ref;	Devel::Peek	B::Deparse
デバッガ(perl -d foo.pl、$ perldoc perldebug)		
