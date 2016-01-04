Title: Relaxed JSON parsing
Date: 2011-12-27 13:40
Author: Attila-Mihaly Balazs
Tags: json, java, jug
Slug: relaxed-json-parsing
Status: published

*This blogpost was originally posted to [the Transylvania JUG
blog](http://www.transylvania-jug.org/archives/324).*

JSON is a good alternative when you need a lightweight format to specify
structured data. But sometimes (for example when you want the user to
specify JSON manually) you would like to relax the formalism required to
specify ["valid" JSON](http://json.org/) data. For example the following
snippet is not valid as per the spec, although its intent is quite
clear:

    [{ foo: 'bar' }]

</code>

To make this standard compliant we would need to write it as:

    [{ "foo": "bar" }]

</code>

We shouldn't run out and blame the standard of course since it needs to
balance many contradictory requirements (ambiguity of encoded data, ease
of understanding, ease of writing parsers, etc). If you decide that you
want to strike the balance differently (make the definition of valid
data more relaxed) you can do this easily with the [Jackson
parser](http://jackson.codehaus.org/):

    JsonParser parser = new JsonFactory()
        .createJsonParser("[{ foo: 'bar' }]")
            .enable(JsonParser.Feature.ALLOW_UNQUOTED_FIELD_NAMES)
            .enable(JsonParser.Feature.ALLOW_SINGLE_QUOTES);
    JsonNode root = new ObjectMapper().readTree(parser);

    assertEquals("bar", root.get(0).get("foo").asText());

</code>

If your tool of choice is [gson](http://code.google.com/p/google-gson/),
it is slightly more complicated but still doable. See the [linked source
code](http://code.google.com/p/hype-free/source/browse/trunk/espresso-shots/src/org/transylvania/jug/espresso/shots/d20111018/TestRelaxedJSONParsing.java)
for a complete example.

JSON is a good tool for semi-structured data and using a relaxed parsing
can make the programs you write easier to use.
