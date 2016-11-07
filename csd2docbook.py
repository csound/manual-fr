# -*- coding: utf-8 -*-
#
# Copyright (C) 2007 Francois Pinot
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA 02111, USA
# or connect to:
# http://www.fsf.org/licensing/licenses/lgpl.html

import ctcsound
import getopt, sys, os, glob, re
import traceback
from xml.dom import minidom

playable = False

class OrchestraDict(dict):
    def __init__(self):
        self.initOpcodes()
        self.initHeaderSymbols()
        self.initBlockDelim()
        self.initOperators()
        self.initSeqCtrl()
        self.initMacros()
        self.labels = []

    def initOpcodes(self):
        '''Read the list of csound opcodes from Csound API.

        Thus we're sure that the opcode list is up to date, however it will be
        complete only if csound has been built with all the plugins.
        It is needed to compile an orchestra and score before calling
        CsoundOpcodeList() in order to get the opcode list. So we use a dummy
        csd string for that purpose (tricky isn't it?)
        '''
        cs = ctcsound.Csound()
        dummy = '''<CsoundSynthesizer>
        <CsOptions>
        -dodac
        </CsOptions>
        <CsInstruments>
        instr 1
          print p3
        endin
        </CsInstruments>
        <CsScore>
        i1 0 1
        e
        </CsScore>
        </CsoundSynthesizer>'''
        cs.compileCsdText("dummy.csd")
        lo, n = cs.newOpcodeList()
        print("{} opcodes registered".format(n))
        for i in range(n):
            self[lo[i].opname] = 'opc'
        del cs

    def initHeaderSymbols(self):
        self.update({
            'sr':'ohdr', 'kr':'ohdr', 'ksmps':'ohdr', 'nchnls':'ohdr',
            '0dbfs':'ohdr', 'ctrlinit':'ohdr', 'ftgen':'ohdr', 'massign':'ohdr',
            'pgmassign':'ohdr', 'seed':'ohdr', 'strset':'ohdr'})

    def initBlockDelim(self):
        self.update({
            'instr':'oblock', 'endin':'oblock',
            'opcode':'oblock', 'endop':'oblock'})

    def initOperators(self):
        self.update({
            '==':'op', '!=':'op', '?':'op', '>':'op', '>=':'op', 'LeSsThAn':'op',
            'LeSsThAn=':'op', '=':'op', '+':'op', '-':'op', '*':'op', '/':'op',
            '%':'op', '^':'op', 'AmPeRsAnDAmPeRsAnD':'op', '||':'op',
            'AmPeRsAnD':'op', '|':'op', '~':'op', ':':'op'})

    def initSeqCtrl(self):
        self.update({
            'cggoto':'octrl', 'cigoto':'octrl', 'ckgoto':'octrl', 'cngoto':'octrl',
            'elseif':'octrl', 'else':'octrl', 'endif':'octrl', 'goto':'octrl',
            'if':'octrl', 'igoto':'octrl', 'kgoto':'octrl', 'tigoto':'octrl',
            'timout':'octrl', 'loop_ge':'octrl', 'loop_gt':'octrl',
            'loop_le':'octrl', 'loop_lt':'octrl'})

    def initMacros(self):
        self.update({
            '#define':'omacro', '#ifdef':'omacro', '#ifndef':'omacro', '#end':'omacro',
            '#else':'omacro', '#include':'omacro', '#undef':'omacro'})

    def addLabel(self, key):
        self[key] = 'olabel'
        self.labels.append(key)

    def clearLabels(self):
        for key in self.labels:
            if key in self:
                self.pop(key)
        self.labels = []

    def get(self, key, x=None):
        if key in self:
            return  '<emphasis role="' + self[key] +'">' + key + '</emphasis>'
        return key

class OrchestraTransform(object):
    def __init__(self):
        motif = '''(
          \s+ | \( |
          == | != | LeSsThAn= | LeSsThAn | >= | > | \? |
          = | \+ | - | \* | / | % | ^ |
          AmPeRsAnDAmPeRsAnD | \|\| |
          AmPeRsAnD | \| | ~ | :
          )'''
        self.pattern = re.compile(motif, re.VERBOSE)
        self.labelPattern = re.compile('[a-zA-Z]\w*:')
        self.orcDict = OrchestraDict()

    def detectLabels(self, lines):
        for s in lines:
            c = self.labelPattern.match(s)
            if c:
                self.orcDict.addLabel(s[:c.end()-1])

    def comment(self, s):
        return '<emphasis role="comment">' + s + '</emphasis>'

    def orcLine(self, line):
        inTokens = self.pattern.split(line)
        outTokens = []
        for t in inTokens:
            if len(t) > 0:
                outTokens.append(self.orcDict.get(t, line))
        return ''.join(outTokens)

    def transformLines(self, lines):
        self.orcDict.clearLabels()
        self.detectLabels(lines)
        outLines = []
        for s in lines:
            i = s.find(';')
            if i == 0:
                outLines.append(self.comment(s))
            elif i > 0:
                outLines.append(self.orcLine(s[:i]) + self.comment(s[i:]))
            else:
                outLines.append(self.orcLine(s))
        return outLines

    def transform(self, filename):
        f = open(filename, 'r')
        s = f.read()
        f.close()
        s = s.replace('&', 'AmPeRsAnD')
        s = s.replace('<', 'LeSsThAn')
        s = s.replace('LeSsThAnCs', '<Cs')
        s = s.replace('LeSsThAn/Cs', '</Cs')
        olines = self.transformLines(s.split('\n'))
        s = '\n'.join(olines).replace('AmPeRsAnD', '&amp;')
        s = s.replace('LeSsThAn', '&lt;')
        outfn = filename.replace('examples', 'examples-xml')
        fout = open(outfn + '.xml', 'w')
        fout.write('<programlisting>\n')
        fout.write(s)
        fout.write('</programlisting>')
        fout.close()
        print(filename)

class ScoreTransform(object):
    def __init__(self):
        self.pattern = re.compile('^\s*[abefimnqrstvx]')

    def comment(self, s):
        return '<emphasis role="comment">' + s + '</emphasis>'

    def scoLine(self, line):
        r = self.pattern.search(line)
        if r:
            s = line[r.end()-1]
            return line.replace(s, '<emphasis role="stamnt">' + s + '</emphasis>')
        return line

    def transformLines(self, lines):
        outLines = []
        for s in lines:
            i = s.find(';')
            if i == 0:
                outLines.append(self.comment(s))
            elif i > 0:
                outLines.append(self.scoLine(s[:i]) + self.comment(s[i:]))
            else:
                outLines.append(self.scoLine(s))
        return outLines

class CsdTransform(object):
    def __init__(self, playable=False):
        self.orc_t = OrchestraTransform()
        self.sco_t = ScoreTransform()
        self.playable = playable

    def text(self, node):
        s = node.childNodes[0].nodeValue
        if s[0] == '\n':
            start = 1
        else:
            start = 0
        if s[-1] == '\n':
            end = -1
        else:
            end = None
        return s[start:end].split('\n')

    def optTransform(self, lines):
        comment = lambda s: '<emphasis role="comment">' + s + '</emphasis>'
        outLines = []
        for s in lines:
            i = s.find(';')
            if i == 0:
                outLines.append(comment(s))
            elif i > 0:
                outLines.append(s[:i] + comment(s[i:]))
            else:
                outLines.append(s)
        return outLines

    def write_playable_example(self, filename, text):
        try:
            html_filename = filename + '.html'
            print("Writing playable example: {}".format(html_filename))
            fout = open(html_filename, 'w')
            chunk = '''<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>adsr</title>
<link rel="stylesheet" type="text/css" href="csound.css" />
<meta name="generator" content="DocBook XSL Stylesheets V1.78.1" />
<link rel="home" href="index.html" title="The Canonical Csound Reference Manual" />
<link rel="up" href="OpcodesTop.html" title="Orchestra Opcodes and Operators" />
<link rel="prev" href="active.html" title="active" />
<link rel="next" href="adsyn.html" title="adsyn" />
</head>
<h1>'''
            fout.write(chunk)
            fout.write(html_filename)
            chunk = '''</h1>
<p>
This example will play if your Web browser is a desktop version of Google Chrome with PNaCl enabled. You can edit and replay the code. At this time, most but not all examples will run in PNaCl.
</p>
<p>
<input type="button" value="Play" onclick="start_onclick()"/>
<input type="button" value="Stop" onclick="stop_onclick()"/>
<p>
<textarea id="csd" style="width: 100%; height: 50%;font-size:12px;">'''
            fout.write(chunk)
            fout.write(text)
            chunk = '''</textarea>
<h3>Csound Messages</h3>
<textarea id="console" readonly style="width: 100%; height: 25%;font-size:12px;">
</textarea>
<script type="text/javascript" src="../../csound.js"></script>
<script>
function handleMessage(message) {
    console.log(message);
    var messages_textarea = document.getElementById("console");
    var existing = messages_textarea.value;
    messages_textarea.value = existing + message.data;
    messages_textarea.scrollTop = messages_textarea.scrollHeight;
}
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}
function start_onclick() {
    csound.stop();
    sleep(500).then(() => {
        var csd = document.getElementById('csd').value;
        csound.compileCsdText(csd);
    })
}
function stop_onclick () {
    csound.stop();
}
</script>
 <div id="engine"></div>
</body>
</html>'''
            fout.write(chunk)
            fout.close()
        except:
            print('Exception on chunk: {}'.format(chunk))
            traceback.print_exc()

    def transform(self, filename):
        tag = lambda s: '<emphasis role="csdtag">&lt;' + s + '&gt;</emphasis>'
        f = open(filename, 'r')
        print(filename)
        s = f.read()
        if self.playable == True:
            self.write_playable_example(filename, s)
        f.close()
        # We convert & and < in "pseudo" entities because we don't want that
        # minidom resolves those entities
        s = s.replace('&', 'AmPeRsAnD')
        s = s.replace('<', 'LeSsThAn')
        s = s.replace('LeSsThAnCs', '<Cs')
        s = s.replace('LeSsThAn/Cs', '</Cs')
        try:
            csddoc = minidom.parseString(s)
        except:
            print("Exception on s: {}".format(s))
            traceback.print_exc()
            return
        optionsPresent = True
        try:
            options = csddoc.getElementsByTagName("CsOptions")[0]
        except:
            optionsPresent = False
        orchestra = csddoc.getElementsByTagName("CsInstruments")[0]
        score = csddoc.getElementsByTagName("CsScore")[0]
        outLines = []
        outLines.append('<refsect1>')
        if self.playable == True:
            outLines.append('<ulink url="%s.html">Play</ulink>' % filename);
        outLines.append('<programlisting>')
        outLines.append(tag("CsoundSynthesizer"))
        if optionsPresent:
            outLines.append(tag("CsOptions"))
            outLines.extend(self.optTransform(self.text(options)))
            outLines.append(tag("/CsOptions"))
        outLines.append(tag("CsInstruments"))
        outLines.extend(self.orc_t.transformLines(self.text(orchestra)))
        outLines.append(tag("/CsInstruments"))
        outLines.append(tag("CsScore"))
        outLines.extend(self.sco_t.transformLines(self.text(score)))
        outLines.append(tag("/CsScore"))
        outLines.append(tag("/CsoundSynthesizer"))
        outLines.append('</programlisting>')
        outLines.append('</refsect1>')
        csddoc.unlink()
        # We convert back our "pseudo" entities in actual entities
        s = '\n'.join(outLines).replace('AmPeRsAnD', '&amp;')
        s = s.replace('LeSsThAn', '&lt;')
        s += '\n'
        outfn = filename.replace('examples', 'examples-xml')
        fout = open(outfn + '.xml', 'w')
        fout.write(s)
        fout.close()


def main():
    """Usage: python csd2xml options [filename]

    where options are one or more of the following:
        -f filename or --file=filename
            Transform examples/filename to examples-xml/filename.xml
            where filename is the name of a csd file or orc file
        -a or --all
            Transform all the csd files of the example directory to
            xml files in the examples-xml directory.
        --pnacl
            Create a link to a version of each example csd that is
            playable using Csound for PNaCl."""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:a", ["file=", "all", "pnacl"])
    except getopt.GetoptError:
        print(main.__doc__)
        sys.exit(2)
    playable = '--pnacl' in sys.argv[1:]
    print("playable: {}".format(playable))
    for o, a in opts:
        if o in ("-f", "--file") and a:
            if a.find('examples') < 0:
                a = 'examples' + os.sep + a
            if os.path.exists(a):
                suf = os.path.splitext(a)[1]
                if suf == '.csd':
                    CsdTransform(playable).transform(a)
                elif suf == '.orc':
                    OrchestraTransform().transform(a)
                else:
                    print( a + " is not a csd or orc filename")
                sys.exit(0)
            else:
                print(a + " doesn't exist!")
                sys.exit(2)
        if o in ("-a", "--all"):
            ct = CsdTransform(playable)
            infiles = glob.glob('examples/*.csd')
            for f in infiles:
                ct.transform(f)
            sys.exit(0)
    print(main.__doc__)
    sys.exit(2)


if __name__ == '__main__':
    main()

