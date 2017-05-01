
This test case shows an issue with pubnub where the actual exit of the program takes
a few *minutes* (not seconds, as I'd expect).  I'm running it on my laptop (a Macbook Pro).

See run.txt for 10 runs of the test.  For example, this snippet:

`done! 2017-04-30 19:42:09.836880`
`Sun Apr 30 19:46:45 PDT 2017`

Shows that it took over 4 minutes from the time the last like was executed until the program actually stopped 
and returned control back to the console.
