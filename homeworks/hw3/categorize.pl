#!/usr/bin/perl

# Author: Kuba Gasiorowski
# Last edited: Nov 15th, 2019
# netID: kgasiorowski
# sbuID: 109776237

use warnings;
use strict;

my $input_file = $ARGV[0];

open INPUT, "<".$input_file or die("Couldn't open input file $input_file");

open EFILE, ">efiles.txt";
open RFILE, ">rfiles.txt";
open WFILE, ">wfiles.txt";
open XFILE, ">xfiles.txt";
open TFILE, ">tfiles.txt";

my @efiles;
my @rfiles;
my @wfiles;
my @xfiles;
my @tfiles;

while(my $line = <INPUT>){

        chomp($line);

        if(-e $line){

                print EFILE $line."\n";
                push @efiles, $line;

        }

        if(-r $line){

                print RFILE $line."\n";
                push @rfiles, $line;

        }

        if(-w $line){

                print WFILE $line."\n";
                push @wfiles, $line;

        }

        if(-x $line){

                print XFILE $line."\n";
                push @xfiles, $line;

        }

        if(-t $line){

                print TFILE $line."\n";
                push @tfiles, $line;

        }


}

print scalar @efiles." existing files: @efiles\n";
print scalar @rfiles." readable files: @rfiles\n";
print scalar @wfiles." writable files: @wfiles\n";
print scalar @xfiles." executable files: @xfiles\n";
print scalar @tfiles." text files: @tfiles\n";

close INPUT;

close EFILE;
close RFILE;
close WFILE;
close XFILE;
close TFILE;