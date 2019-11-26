#!/usr/bin/perl

# Author: Kuba Gasiorowski
# Last edited: Nov 15th, 2019
# netID: kgasiorowski
# sbuID: 10977237

use warnings;
use strict;

my $file = $ARGV[0];
my $line;

open(FILE, $file);

while($line =<FILE>){

        # print $line;

        $line =~ s/<p>(.*)<\/p>/$1<br><br>/g;
        $line =~ s/<span>|<\/span>//g;
        print $line;

}