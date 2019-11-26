#!/usr/bin/perl

# Author: Kuba Gasiorowski
# Last edited: Nov 15th, 2019
# netID: kgasiorowski
# sbuID: 109776237

use warnings;
use strict;

my $output = qx/echo \$PATH/;
chomp($output);
foreach($output =~ m/[^:]+/g){

        print("$_\n");

}