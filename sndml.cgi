#!/usr/bin/perl
# 161102 re-create sndml.cgi for xre,tk2
$sendmail = '/usr/lib/sendmail';
use Encode;
Encode=from_to($_,'utf8'); 

$to="   ";		$from="foo@bar.com";	$subject ="  ";	$mailbody="  ";

print "Content-type: text/html\n\n";

print "<form ><input><><>"<>";

open(MAIL,"| $sendmail -t");
print MAIL "To: $to\n","From: $from\n","Subject:$subject\n\n",$mailbody;
close(MAIL);

__END__
# sample by [簡単cgi]>PerlTips>メール送信 http://easycgi.xrea.jp/perltips/mail1.htm
# xrea perl(V5.6/5.8) /usr/bin/perl or /usr/local/bin/perl
#      php5-7.0 /usr/local/bin/php... (CGI-PHP7.0-5.3含む)
#      python /usr/local/bin/python
# ruby /usr/local/bin/ruby
# sendmail /usr/sbin/sendmail
# use Jcode;  $str2=Jcode::convert($str1,'utf8'[,'sjis']);  #utf8->sjis
# use Encode; from_to($str,'utf8','shiftjis'); #utf8->shiftjis, Perl5.8.0over
