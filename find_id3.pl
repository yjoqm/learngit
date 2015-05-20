#!/usr/bin/perl
my %hash;
open FILE,shift or die"file error";
while (<FILE>){
	chomp;
	my $id= $1 if /finish (\d+)/;
	print STDERR "xml_id:".$id." ";
	$hash{$id}++;
}

foreach (sort{$hash{$b}<=>$hash{$a}} keys %hash){print $_."---".$hash{$_}."\n";}
