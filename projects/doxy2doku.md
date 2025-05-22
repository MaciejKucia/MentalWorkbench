# Doxygen XML to DokuWiki XLS transformation

Doxygen is a great tool that properly used can save significant amount of time during software development. Doxygen can process data using limited number of output formats. Thankfully it can generate XML output that can be converted into any format.

I am using [XSLT](https://en.wikipedia.org/wiki/XSLT) to generate dokuwiki page.

## Step 1: Build Doxygen XML files

I like to use doxywizard.

## Step 2: Merge XML files into single one

`*msxsl.exe ./xml/index.xml ./xml/combine.xslt -o ./xml/combined.xml*`

## Step 3: Build DokuWiki textfiles

`*msxsl.exe ./xml/combined.xml transform.xsl -o wikipage.txt*`

## Step 4: Copy DokuWiki files

To the dokuwiki pages directory.

## Summary

* [doxwiki.zip](/media/doxwiki.zip)

### References

* <http://www.w3schools.com/xsl/>
* <http://www.w3.org/TR/xslt>
