Title: Unshortifying Cisco “Go” links
Date: 2010-03-19 17:23
Author: Attila-Mihaly Balazs
Tags: http, perl, html, cisco, web
Slug: unshortifying-cisco-go-links
Status: published

Inspired by a post on the PacketLife.net blog - [Cisco "Go" links
reference in the
wiki](http://packetlife.net/blog/2010/mar/6/cisco-go-links-reference-wiki/)
– I tried to mine the short links to come up with the “definitive” list,
but after running it for a couple of days, it only managed to find 473
links, compared to the 4720 [Google
estimates](http://www.google.com/search?hl=en&q=site%3Acisco.com+inurl%3A%2Fgo%2F)
it has ([Yahoo
estimates](http://search.yahoo.com/search?p=site%3Acisco.com+inurl%3A%2Fgo%2F)
4200, but it seems to include more non-relevant results – or maybe I
don’t know to use the search operators on it correctly :-P). Anyway, I
thought that the code might be useful for somebody doing other scraping
projects, so you can [find it in my Google Code SVN
repository](http://code.google.com/p/hype-free/source/browse/trunk/cisco_unshortify_links.pl).
It illustrates a couple of techniques:

-   Generating all the combinations from a given alphabet in a simple
    and fast manner
-   Using multi-threading to increase performance and reduce the time
    wasted by waiting for network I/O.
-   How to fetch gzip-ed content (any well-behaved spider should offer
    the site the option to do so to conserve their bandwidth) using
    LWP::UserAgent (I found it thanks to [this StackOverflow
    question](http://stackoverflow.com/questions/1285305/how-can-i-accept-gzip-compressed-content-using-lwpuseragent))

Check it out if you have a similar problem!

Finally, below you have the list of links. A quick look reveals two
interesting observations: there are duplicates (multiple links pointing
to the same page) and some of the links point to non-Cisco pages.

http://cisco.com/go/f =\> [Redirect page - Cisco
Systems](http://www.cisco.com/web/mobile/fed/)(http://www.cisco.com/web/mobile/fed/)  
http://cisco.com/go/m =\> [Cisco Systems - Cisco Speaking Sessions at
Mobile World
Congress](http://www.cisco.com/web/learning/le21/le34/MWC/2009/mobi/)
(http://www.cisco.com/web/learning/le21/le34/MWC/2009/mobi/)  
http://cisco.com/go/n =\> [Cisco Systems -
Innovators](http://www.cisco.com/web/mobile/nws/)
(http://www.cisco.com/web/mobile/nws/)  
http://cisco.com/go/s =\> [Cisco Systems - Test Your Cisco
Smarts](http://www.cisco.com/web/mobile/s/)
(http://www.cisco.com/web/mobile/s/)  
http://cisco.com/go/ea =\> [Cisco Unified Expert Advisor - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9675/index.html)
(http://www.cisco.com/en/US/products/ps9675/index.html)  
http://cisco.com/go/sa =\> [Cisco IOS Software Activation - Cisco
Systems](http://www.cisco.com/en/US/products/ps9677/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps9677/products\_ios\_technology\_home.html)  
http://cisco.com/go/qb =\> [Cisco
Systems](http://www.cisco.com/web/partners/quotebuilder)(http://www.cisco.com/web/partners/quotebuilder)  
http://cisco.com/go/ac =\> [Cisco Systems - Unified Attendant Console
solutions](http://cisco-ac.arcsolutions.com)
(http://cisco-ac.arcsolutions.com)  
http://cisco.com/go/cc =\> [Customer Contact - Cisco
Systems](http://www.cisco.com/en/US/products/sw/custcosw/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/sw/custcosw/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/bc =\> [SA Europe -
Broadcasters/Programmers](http://www.saeurope.com/solutions/broadcasters.htm)
(http://www.saeurope.com/solutions/broadcasters.htm)  
http://cisco.com/go/dc =\> [Data Center - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns340/ns394/ns224/index.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns224/index.html)  
http://cisco.com/go/pc =\> [Positive Connections - Operational
Excellence through Connected Manufacturing, 19 May 2009, 9am-12pm GMT
Webcast](http://www.cisco.com/web/offer/emea/positiveconnections/index.html)
(http://www.cisco.com/web/offer/emea/positiveconnections/index.html)  
http://cisco.com/go/uc =\> [Voice & Unified Communications - Main Page -
Cisco
Systems](http://www.cisco.com/en/US/products/sw/voicesw/index.html)
(http://www.cisco.com/en/US/products/sw/voicesw/index.html)  
http://cisco.com/go/vc =\> [VoiceCon 2010 - Cisco Events - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)(http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)  
http://cisco.com/go/id =\> [Cisco Systems,
Inc](http://www.cisco.com/web/ID/index.html)
(http://www.cisco.com/web/ID/index.html)  
http://cisco.com/go/ce =\> [Carrier Ethernet - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns577/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns577/networking\_solutions\_solution.html)  
http://cisco.com/go/ie =\> [Cisco Catalyst 2955 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6738/index.html)
(http://www.cisco.com/en/US/products/ps6738/index.html)  
http://cisco.com/go/3g =\> [Cisco 3G Wireless Connectivity Solutions 
[Cisco 800 Series Routers] - Cisco
Systems](http://www.cisco.com/en/US/prod/routers/ps380/3g_solns.html)
(http://www.cisco.com/en/US/prod/routers/ps380/3g\_solns.html)  
http://cisco.com/go/ph =\> [Partner Helpline - Partner Central - Cisco
Systems](http://www.cisco.com/web/partners/tools/helponline/index.html)(http://www.cisco.com/web/partners/tools/helponline/index.html)  
http://cisco.com/go/dm =\> [Order Direct From Cisco - Cisco
Systems](http://www.cisco.com/commarch/cvs/dm)
(http://www.cisco.com/commarch/cvs/dm)  
http://cisco.com/go/sm =\> [Cisco Systems - Redirect
to](http://www.cisco.com/humannetwork)
(http://www.cisco.com/humannetwork)  
http://cisco.com/go/hn =\> [The Human Network - Cisco
Systems](http://www.cisco.com/web/thehumannetwork/index1.html?POSITION=link&COUNTRY_SITE=us&CAMPAIGN=HN2&CREATIVE=HN2+to+HN1&REFERRING_SITE=CISCO%2ECOM+HN2+Microsite)
(http://www.cisco.com/web/thehumannetwork/index1.html?POSITION=link&COUNTRY;\_SITE=us&CAMPAIGN;=HN2&CREATIVE;=HN2+to+HN1&REFERRING;\_SITE=CISCO%2ECOM+HN2+Microsite)  
http://cisco.com/go/fn =\> [Cisco Feature Navigator - Cisco
Systems](http://tools.cisco.com/ITDIT/CFN/jsp/index.jsp)
(http://tools.cisco.com/ITDIT/CFN/jsp/index.jsp)  
http://cisco.com/go/sn =\> [Cisco.com Login
Page](http://tools.cisco.com/Support/CPI/index.do)
(http://tools.cisco.com/Support/CPI/index.do)  
http://cisco.com/go/so =\> [Cisco Learning Partner Associate - Learning
Partners Program Overview - Cisco
Systems](http://www.cisco.com/web/learning/le27/le53/learning_partner_so.html)(http://www.cisco.com/web/learning/le27/le53/learning\_partner\_so.html)  
http://cisco.com/go/cp =\> [Cisco Powered Program - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns206/networking_solutions_solution_category.html)
(http://www.cisco.com/en/US/netsol/ns206/networking\_solutions\_solution\_category.html)  
http://cisco.com/go/bp =\> [Cisco
Systems](http://www.cisco.com/web/partners/program/other/brand-protection/index.html)(http://www.cisco.com/web/partners/program/other/brand-protection/index.html)  
http://cisco.com/go/ds =\> [Cisco Digital Signs - Cisco
Systems](http://www.cisco.com/web/solutions/dms/digital_signage.html)(http://www.cisco.com/web/solutions/dms/digital\_signage.html)  
http://cisco.com/go/ps =\> [Government and Education - Cisco
Systems](http://www.cisco.com/web/strategy/government_education_index.html)(http://www.cisco.com/web/strategy/government\_education\_index.html)  
http://cisco.com/go/ts =\> [Technical Services - Cisco
Systems](http://www.cisco.com/en/US/products/svcs/ps3034/ps2827/serv_category_home.html)
(http://www.cisco.com/en/US/products/svcs/ps3034/ps2827/serv\_category\_home.html)  
http://cisco.com/go/tv =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/x2 =\> [Cisco Systems - Redirect
to](http://www.cisco.com/en/US/products/hw/modules/ps5455/products_data_sheet0900aecd801f92aa.html)
(http://www.cisco.com/en/US/products/hw/modules/ps5455/products\_data\_sheet0900aecd801f92aa.html)  
http://cisco.com/go/24 =\> [President Taylor Meets Over TelePresence On
24 - Video Detail - The Video
Lounge](http://videolounge.cisco.com/video/24-pres-taylor-meets-over-tp/?Referring_site=PrintTv&Country_Site=US&Campaign=HN&Position=URL&Creative=go/24&Where=go/24)
(http://videolounge.cisco.com/video/24-pres-taylor-meets-over-tp/?Referring\_site=PrintTv&Country;\_Site=US&Campaign;=HN&Position;=URL&Creative;=go/24&Where;=go/24)  
http://cisco.com/go/saa =\> [Cisco IOS IP Service Level Agreements
(SLAs) - Cisco
Systems](http://www.cisco.com/en/US/products/ps6602/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6602/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/cca =\> [Cisco NAC Appliance (Clean Access) -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6128/index.html)
(http://www.cisco.com/en/US/products/ps6128/index.html)  
http://cisco.com/go/pda =\> [Cisco Systems,
Inc](http://www.cisco.com/cdc_content_elements/mobile/)
(http://www.cisco.com/cdc\_content\_elements/mobile/)  
http://cisco.com/go/sea =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/strategy/transportation/seaports.html)
(http://www.cisco.com/en/US/strategy/transportation/seaports.html)  
http://cisco.com/go/cia =\> [Collaboration In
Action](http://www.cisco.com/web/offer/emea/collaborationinaction)
(http://www.cisco.com/web/offer/emea/collaborationinaction)  
http://cisco.com/go/via =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns341/ns396/ns166/ns68/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns341/ns396/ns166/ns68/networking\_solutions\_solution.html)  
http://cisco.com/go/ana =\> [Cisco Active Network Abstraction - Products
& Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6776/index.html)
(http://www.cisco.com/en/US/products/ps6776/index.html)  
http://cisco.com/go/cna =\> [Cisco Network Assistant - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5931/index.html)
(http://www.cisco.com/en/US/products/ps5931/index.html)  
http://cisco.com/go/cpa =\> [Cisco Channel Port Adapter - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/modules/ps2033/ps124/index.html)
(http://www.cisco.com/en/US/products/hw/modules/ps2033/ps124/index.html)  
http://cisco.com/go/lpa =\> [Cisco Learning Partner Associate - Learning
Partners Program Overview - Cisco
Systems](http://www.cisco.com/web/learning/le27/le53/learning_partner_so.html)(http://www.cisco.com/web/learning/le27/le53/learning\_partner\_so.html)  
http://cisco.com/go/spa =\> [Cisco Shared Port Adapters/SPA Interface
Processors - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6267/prod_module_series_home.html)
(http://www.cisco.com/en/US/products/ps6267/prod\_module\_series\_home.html)  
http://cisco.com/go/cqa =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/quoteadvisor.html)(http://www.cisco.com/web/partners/sell/technology/quoteadvisor.html)  
http://cisco.com/go/asa =\> [Cisco ASA 5500 Series Adaptive Security
Appliances - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6120/index.html)
(http://www.cisco.com/en/US/products/ps6120/index.html)  
http://cisco.com/go/csa =\> [Cisco Security Agent - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/secursw/ps5057/index.html)
(http://www.cisco.com/en/US/products/sw/secursw/ps5057/index.html)  
http://cisco.com/go/isa =\> [CCO Decommission
Page](http://www.cisco.com/warp/public/732/Tech/connectivity/ssg/)
(http://www.cisco.com/warp/public/732/Tech/connectivity/ssg/)  
http://cisco.com/go/msa =\> [Introduction - Cisco
Systems](http://www.cisco.com/en/US/partners/pr67/pr41/pr263/partners_strategic_solution_concept_home.html)(http://www.cisco.com/en/US/partners/pr67/pr41/pr263/partners\_strategic\_solution\_concept\_home.html)  
http://cisco.com/go/vsa =\> [Cisco VPN Services Adapter - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7332/index.html)
(http://www.cisco.com/en/US/products/ps7332/index.html)  
http://cisco.com/go/cta =\> [NAC - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns466/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns466/networking\_solutions\_package.html)  
http://cisco.com/go/aya =\> [Are You Attached Seminar Series - 1
Day](https://programs.regweb.com/cisco/aya/)
(https://programs.regweb.com/cisco/aya/)  
http://cisco.com/go/cab =\> [Cisco.com Login
Page](http://forums.cisco.com/eforum/servlet/CAB?page=main&sn=CAB)
(http://forums.cisco.com/eforum/servlet/CAB?page=main&sn;=CAB)  
http://cisco.com/go/mib =\> [Cisco IOS MIB
Locator](http://tools.cisco.com/ITDIT/MIBS/servlet/index)
(http://tools.cisco.com/ITDIT/MIBS/servlet/index)  
http://cisco.com/go/sib =\> [Small is
BIG](http://www.cisco.com/web/EA/sib/index.html)
(http://www.cisco.com/web/EA/sib/index.html)  
http://cisco.com/go/brb =\> [Branch - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns477/index.html)
(http://www.cisco.com/en/US/netsol/ns477/index.html)  
http://cisco.com/go/irb =\> [Thought Leadership
Network](http://newsroom.cisco.com/dlls/tln/redirects/irb_metric.html)
(http://newsroom.cisco.com/dlls/tln/redirects/irb\_metric.html)  
http://cisco.com/go/fsb =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns477/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns477/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/hsb =\> [Cisco Hosted Small Business
Communications - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns1028/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns1028/networking\_solutions\_solution.html)  
http://cisco.com/go/twb =\> [Teachers Without
Borders](http://www.cisco.com/web/learning/netacad/landing/TWB.html)
(http://www.cisco.com/web/learning/netacad/landing/TWB.html)  
http://cisco.com/go/syb =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/security/secure_your_branch.html)(http://www.cisco.com/web/partners/sell/technology/security/secure\_your\_branch.html)  
http://cisco.com/go/dac =\> [Cisco Unified Department Attendant
Console - Cisco
Systems](http://www.cisco.com/en/US/products/ps7295/index.html)
(http://www.cisco.com/en/US/products/ps7295/index.html)  
http://cisco.com/go/eac =\> [Cisco Physical Access Gateways - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9687/index.html)
(http://www.cisco.com/en/US/products/ps9687/index.html)  
http://cisco.com/go/nac =\> [NAC - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns466/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns466/networking\_solutions\_package.html)  
http://cisco.com/go/ibc =\> [Join Us at IBC
2009](http://www.scientificatlanta.com/email/2009/0709-IBC/new/JoinCiscoatIBC2009.htm)
(http://www.scientificatlanta.com/email/2009/0709-IBC/new/JoinCiscoatIBC2009.htm)  
http://cisco.com/go/nbc =\> [30 Rock/Jenna Finds A Flip - Video Detail -
The Video
Lounge](http://videolounge.cisco.com/video/30-rockjenna-finds-a-flip/?Referring_site=PrintTV&Country_Site=US&Campaign=Product+Integrations&Position=Vanity&Creative=http://www.cisco.com/go/nbc)
(http://videolounge.cisco.com/video/30-rockjenna-finds-a-flip/?Referring\_site=PrintTV&Country;\_Site=US&Campaign;=Product+Integrations&Position;=Vanity&Creative;=http://www.cisco.com/go/nbc)  
http://cisco.com/go/sbc =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns759/networking_solutions_sub_sub_solution.html)
(http://www.cisco.com/en/US/netsol/ns759/networking\_solutions\_sub\_sub\_solution.html)  
http://cisco.com/go/pec =\> [Partner Education Connection - Training
Resources - Cisco
Systems](http://www.cisco.com/web/learning/le36/learning_partner_e-learning_connection_tool_launch.html)(http://www.cisco.com/web/learning/le36/learning\_partner\_e-learning\_connection\_tool\_launch.html)  
http://cisco.com/go/cfc =\> [Order Direct From Cisco - Cisco
Systems](http://www.cisco.com/commarch/cvs/cfc)
(http://www.cisco.com/commarch/cvs/cfc)  
http://cisco.com/go/dfc =\>
[Log-In](http://resources.cisco.com/app/channel-site-builder.taf?channel_id=32631&public_view=true&asset_id=5926)
(http://resources.cisco.com/app/channel-site-builder.taf?channel\_id=32631&public;\_view=true&asset;\_id=5926)  
http://cisco.com/go/cic =\> [Cisco Info Center - Products & Services -
Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/ps996/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/ps996/index.html)  
http://cisco.com/go/tlc =\> [Federal IT Thought Leadership - Industry
Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/government/federal_thought_leadership.html)(http://www.cisco.com/web/strategy/government/federal\_thought\_leadership.html)  
http://cisco.com/go/bmc =\> [DC Partner - BMC - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns957/index.html)
(http://www.cisco.com/en/US/netsol/ns957/index.html)  
http://cisco.com/go/pmc =\> [Cisco
Systems](http://www.cisco.com/web/partners/services/resources/pmc/index.html)(http://www.cisco.com/web/partners/services/resources/pmc/index.html)  
http://cisco.com/go/anc =\> [Inventory and Reporting - Cisco
Systems](http://www.cisco.com/kobayashi/support/home.htm)
(http://www.cisco.com/kobayashi/support/home.htm)  
http://cisco.com/go/voc =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/customer/ordering/o44/ordering_concept_home.html)
(http://www.cisco.com/en/US/customer/ordering/o44/ordering\_concept\_home.html)  
http://cisco.com/go/epc =\> [Cisco IOS Embedded Packet Capture - Cisco
Systems](http://www.cisco.com/en/US/products/ps9913/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps9913/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/ipc =\> [Unified Communications/Voice Solutions -
Cisco
Systems](http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/hpc =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns500/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns500/networking\_solutions\_package.html)  
http://cisco.com/go/rrc =\> [Financial Services - Industry Solutions -
Cisco
Systems](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/isc =\> [Cisco IP Solution Center - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/ps4748/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/ps4748/index.html)  
http://cisco.com/go/psc =\> [Partner Help Online-Partners & Resellers -
Cisco
Systems](http://ciscopsc.custhelp.com/cgi-bin/ciscopsc.cfg/php/enduser/cisco.php)
(http://ciscopsc.custhelp.com/cgi-bin/ciscopsc.cfg/php/enduser/cisco.php)  
http://cisco.com/go/ssc =\> [Partner Help Online-Partners & Resellers -
Cisco
Systems](http://ciscopsc.custhelp.com/cgi-bin/ciscopsc.cfg/php/enduser/cisco.php)
(http://ciscopsc.custhelp.com/cgi-bin/ciscopsc.cfg/php/enduser/cisco.php)  
http://cisco.com/go/cuc =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns641/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns641/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/mwc =\> [Cisco Mobile Wireless Center - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/ps820/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/ps820/index.html)  
http://cisco.com/go/iad =\> [Cisco IAD2400 Series Integrated Access
Devices - Cisco
Systems](http://www.cisco.com/en/US/products/hw/gatecont/ps887/index.html)
(http://www.cisco.com/en/US/products/hw/gatecont/ps887/index.html)  
http://cisco.com/go/fed =\> [e-government - U.S. Federal
Government -Industry Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/government/us_federal.html)(http://www.cisco.com/web/strategy/government/us\_federal.html)  
http://cisco.com/go/cmd =\> [Cisco Monitor Director - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7246/index.html)
(http://www.cisco.com/en/US/products/ps7246/index.html)  
http://cisco.com/go/usd =\> [Cisco Unified Service
Delivery](http://www.cisco.com/cdc_content_elements/flash/netsol/sp/sdc/index.html?POSITION=printvanity&COUNTRY_SITE=us&CAMPAIGN=SDC&CREATIVE=Vanity&REFERRING_SITE=Vanity+URL)
(http://www.cisco.com/cdc\_content\_elements/flash/netsol/sp/sdc/index.html?POSITION=printvanity&COUNTRY;\_SITE=us&CAMPAIGN;=SDC&CREATIVE;=Vanity&REFERRING;\_SITE=Vanity+URL)  
http://cisco.com/go/cvd =\> [Cisco Validated Design Program - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns741/networking_solutions_program_home.html)
(http://www.cisco.com/en/US/netsol/ns741/networking\_solutions\_program\_home.html)  
http://cisco.com/go/ace =\> [Data Center Application Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5719/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps5719/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/dce =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns783/networking_solutions_package.html#~overview)
(http://www.cisco.com/en/US/netsol/ns783/networking\_solutions\_package.html\#\~overview)  
http://cisco.com/go/nce =\> [Cisco Network Capacity Expansion - Products
& Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9702/index.html)
(http://www.cisco.com/en/US/products/ps9702/index.html)  
http://cisco.com/go/tce =\> [News@Cisco -\> Executive
Biographies](http://tools.cisco.com/dlls/tln/page/business/biz-customer-experience)
(http://tools.cisco.com/dlls/tln/page/business/biz-customer-experience)  
http://cisco.com/go/mde =\> [Cisco MPLS Diagnostics Expert - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6755/index.html)
(http://www.cisco.com/en/US/products/ps6755/index.html)  
http://cisco.com/go/ime =\> [Cisco IPS Manager Express - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9610/index.html)
(http://www.cisco.com/en/US/products/ps9610/index.html)  
http://cisco.com/go/mme =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/partners/pr47/pr288/partners_marketing_made_easy.html)
(http://www.cisco.com/web/partners/pr47/pr288/partners\_marketing\_made\_easy.html)  
http://cisco.com/go/ppe =\> [Cisco.com Login
Page](http://tools.cisco.com/WWChannels/PPP/home.do?actionType=home)
(http://tools.cisco.com/WWChannels/PPP/home.do?actionType=home)  
http://cisco.com/go/ase =\>
[Redirect](http://www.cisco.com/warp/public/437/services/ndm/aes.html)
(http://www.cisco.com/warp/public/437/services/ndm/aes.html)  
http://cisco.com/go/ese =\> [Enterprise - Cisco
Systems](http://www.cisco.com/warp/public/779/largeent/it/ese/srnd.html)
(http://www.cisco.com/warp/public/779/largeent/it/ese/srnd.html)  
http://cisco.com/go/cse =\> [Cisco Solutions
Express](http://www.cisco.com/cdc_content_elements/flash/large_enterprise/truck.html)
(http://www.cisco.com/cdc\_content\_elements/flash/large\_enterprise/truck.html)  
http://cisco.com/go/mse =\> [Cisco 3300 Series Mobility Services
Engine - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9742/index.html)
(http://www.cisco.com/en/US/products/ps9742/index.html)  
http://cisco.com/go/cue =\> [Cisco Unity Express - Cisco
Systems](http://www.cisco.com/en/US/products/sw/voicesw/ps5520/index.html)
(http://www.cisco.com/en/US/products/sw/voicesw/ps5520/index.html)  
http://cisco.com/go/waf =\> [Cisco ACE Web Application Firewall -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9586/index.html)
(http://www.cisco.com/en/US/products/ps9586/index.html)  
http://cisco.com/go/ccf =\> [Network Fabric - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns725/index.html)
(http://www.cisco.com/en/US/netsol/ns725/index.html)  
http://cisco.com/go/pdf =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/smb/programs_and_promotions/pdf.html)(http://www.cisco.com/web/partners/sell/smb/programs\_and\_promotions/pdf.html)  
http://cisco.com/go/sef =\> [Service Exchange Framework - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns746/networking_solutions_sub_solution.html)
(http://www.cisco.com/en/US/netsol/ns746/networking\_solutions\_sub\_solution.html)  
http://cisco.com/go/jmf =\> [We Apologize - 401
Error](http://www.cisco.com/cgi-bin/front.x/jmf/jmf30/jmf30/SelectCountry)(http://www.cisco.com/cgi-bin/front.x/jmf/jmf30/jmf30/SelectCountry)  
http://cisco.com/go/fnf =\> [Flexible NetFlow - Cisco
Systems](http://www.cisco.com/en/US/products/ps6965/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps6965/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/crf =\> [Cisco.com Login
Page](https://tools.cisco.com/WWChannels/MBO/SMB/home.do)
(https://tools.cisco.com/WWChannels/MBO/SMB/home.do)  
http://cisco.com/go/gsf =\> [2010 Government Solutions
Forum](http://www.cisco.com/web/strategy/government/solutionsforum.html)
(http://www.cisco.com/web/strategy/government/solutionsforum.html)  
http://cisco.com/go/atf =\> [Cisco Systems: Business Discussion Forum -
Login](http://forums.cisco.com/eforum/servlet/CBDF?page=cbdf&forum=CBDF%20Forum&topic=Event%20Discussions&CommCmd=MB%3Fcmd%3Ddisplay_location%26location%3D.2cc298a5)
(http://forums.cisco.com/eforum/servlet/CBDF?page=cbdf&forum;=CBDF%20Forum&topic;=Event%20Discussions&CommCmd;=MB%3Fcmd%3Ddisplay\_location%26location%3D.2cc298a5)  
http://cisco.com/go/ctf =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/strategy/government/Public_Sector_Technology_Forum.html)
(http://www.cisco.com/web/strategy/government/Public\_Sector\_Technology\_Forum.html)  
http://cisco.com/go/gtf =\> [News@Cisco -\> Executive
Biographies](http://newsroom.cisco.com/dlls/tln/events/gtf/index.html)
(http://newsroom.cisco.com/dlls/tln/events/gtf/index.html)  
http://cisco.com/go/tmg =\> [Cisco Transceiver Modules - Support - Cisco
Systems](http://www.cisco.com/en/US/products/hw/modules/ps5455/tsd_products_support_series_home.html)
(http://www.cisco.com/en/US/products/hw/modules/ps5455/tsd\_products\_support\_series\_home.html)  
http://cisco.com/go/qrg =\> [Cisco Product Quick Reference Guide - Cisco
Systems](http://www.cisco.com/en/US/prod/qrg/index.html)
(http://www.cisco.com/en/US/prod/qrg/index.html)  
http://cisco.com/go/isg =\> [Cisco Intelligent Services Gateway - Cisco
Systems](http://www.cisco.com/en/US/products/ps6588/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6588/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/ssg =\> [Service Selection Gateway - Cisco
Systems](http://www.cisco.com/en/US/products/ps6589/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6589/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/cug =\> [Cisco Community Central: Community: Cisco
User
Groups](https://www.myciscocommunity.com/community/technology/collaboration/usergroups)
(https://www.myciscocommunity.com/community/technology/collaboration/usergroups)  
http://cisco.com/go/pbi =\> [Support for Nonprofits - Cisco
Systems](http://www.cisco.com/web/about/ac48/pbi.html)(http://www.cisco.com/web/about/ac48/pbi.html)  
http://cisco.com/go/dci =\> [Data Center Interconnect - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns975/index.html)
(http://www.cisco.com/en/US/netsol/ns975/index.html)  
http://cisco.com/go/pci =\> [PCI Compliance - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns625/index.html)
(http://www.cisco.com/en/US/netsol/ns625/index.html)  
http://cisco.com/go/udi =\> [Products & Services Product Identification
Standard - Cisco
Systems](http://www.cisco.com/en/US/products/products_identification_standard.html)
(http://www.cisco.com/en/US/products/products\_identification\_standard.html)  
http://cisco.com/go/aii =\> [Projects - Cisco
Systems](http://www.cisco.com/en/US/about/ac50/ac207/projects/index.html)(http://www.cisco.com/en/US/about/ac50/ac207/projects/index.html)  
http://cisco.com/go/vni =\> [Visual Networking Index - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns827/networking_solutions_sub_solution.html)
(http://www.cisco.com/en/US/netsol/ns827/networking\_solutions\_sub\_solution.html)  
http://cisco.com/go/cpi =\> [Cisco
Systems](http://www.cisco.com/web/partners/news/index.html)(http://www.cisco.com/web/partners/news/index.html)  
http://cisco.com/go/ppi =\> [Cisco.com Login
Page](https://apps.cisco.com/mbrprv/saw.dll?Dashboard)
(https://apps.cisco.com/mbrprv/saw.dll?Dashboard)  
http://cisco.com/go/vpi =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr46/vpi/vpi.html)(http://www.cisco.com/web/partners/pr46/vpi/vpi.html)  
http://cisco.com/go/ipj =\> [The Internet Protocol Journal - ISSN
1944-1134 - Cisco
Systems](http://www.cisco.com/en/US/about/ac123/ac147/about_cisco_the_internet_protocol_journal.html)(http://www.cisco.com/en/US/about/ac123/ac147/about\_cisco\_the\_internet\_protocol\_journal.html)  
http://cisco.com/go/ask =\> [Cisco Support Community: Cisco Support
Community](http://forum.cisco.com/eforum/servlet/NetProf?page=main)
(http://forum.cisco.com/eforum/servlet/NetProf?page=main)  
http://cisco.com/go/pal =\> [Cisco.com Login
Page](http://tools.cisco.com/WWChannels/PAL/index.jsp)
(http://tools.cisco.com/WWChannels/PAL/index.jsp)  
http://cisco.com/go/ccl =\> [Cisco Collaboration - Introduction - Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/ipc/cisco_collaboration.html)(http://www.cisco.com/web/partners/sell/technology/ipc/cisco\_collaboration.html)  
http://cisco.com/go/oil =\> [Oil and Gas - Industry Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/energy/external_oil.html)(http://www.cisco.com/web/strategy/energy/external\_oil.html)  
http://cisco.com/go/etl =\> [News@Cisco -\> Executive
Biographies](http://newsroom.cisco.com/dlls/tln/)
(http://newsroom.cisco.com/dlls/tln/)  
http://cisco.com/go/nam =\> [Network Analysis Module (NAM) Products -
Cisco
Systems](http://www.cisco.com/en/US/products/ps5740/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps5740/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/vam =\>
[Log-In](http://resources.cisco.com/app/tree.taf?asset_id=57360&public_view=true)
(http://resources.cisco.com/app/tree.taf?asset\_id=57360&public;\_view=true)  
http://cisco.com/go/fbm =\> [Forbidden File or
Application](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/ndm =\> [Introduction - Advanced Services
Education - Cisco
Systems](http://www.cisco.com/web/learning/le31/ase/index.html)(http://www.cisco.com/web/learning/le31/ase/index.html)  
http://cisco.com/go/pdm =\> [Cisco PIX Device Manager - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/ps2032/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/ps2032/index.html)  
http://cisco.com/go/eem =\> [Cisco IOS Embedded Event Manager (EEM) -
Cisco
Systems](http://www.cisco.com/en/US/products/ps6815/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6815/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/eim =\> [Cisco Unified E-Mail Interaction Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7236/index.html)
(http://www.cisco.com/en/US/products/ps7236/index.html)  
http://cisco.com/go/pim =\> [IP Multicast - Cisco
Systems](http://www.cisco.com/en/US/products/ps6552/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6552/products\_ios\_technology\_home.html)  
http://cisco.com/go/rim =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/prod/collateral/voicesw/product_promotion0900aec806e252a.html)
(http://www.cisco.com/en/US/prod/collateral/voicesw/product\_promotion0900aec806e252a.html)  
http://cisco.com/go/wim =\> [Cisco Unified Web Interaction Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7233/index.html)
(http://www.cisco.com/en/US/products/ps7233/index.html)  
http://cisco.com/go/clm =\> [Cisco License Manager - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7138/index.html)
(http://www.cisco.com/en/US/products/ps7138/index.html)  
http://cisco.com/go/cmm =\> [Cisco Multicast Manager - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6337/index.html)
(http://www.cisco.com/en/US/products/ps6337/index.html)  
http://cisco.com/go/anm =\> [Cisco Application Networking Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6904/index.html)
(http://www.cisco.com/en/US/products/ps6904/index.html)  
http://cisco.com/go/enm =\> [Network Management - Main Page - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)  
http://cisco.com/go/com =\> [Order Direct From Cisco - Cisco
Systems](http://www.cisco.com/commarch/cvs/com)
(http://www.cisco.com/commarch/cvs/com)  
http://cisco.com/go/fpm =\> [Cisco IOS Flexible Packet Matching (FPM) -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6723/index.html)
(http://www.cisco.com/en/US/products/ps6723/index.html)  
http://cisco.com/go/epm =\> [Cisco Policy Management - Cisco
Systems](http://www.cisco.com/en/US/products/ps9519/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps9519/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/bqm =\> [Cisco Bandwidth Quality Manager - Network
Planning - Products & Services - Cisco Systems - Cisco
Systems](http://www.cisco.com/en/US/products/ps6385/index.html)
(http://www.cisco.com/en/US/products/ps6385/index.html)  
http://cisco.com/go/asm =\> [Cisco AnyConnect Secure Mobility Solution -
Cisco Systems](http://www.cisco.com/en/US/netsol/ns1049/index.html)
(http://www.cisco.com/en/US/netsol/ns1049/index.html)  
http://cisco.com/go/lsm =\> [IP Multicast - Cisco
Systems](http://www.cisco.com/en/US/products/ps6552/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6552/products\_ios\_technology\_home.html)  
http://cisco.com/go/ctm =\> [Cisco Transport Manager - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/opticsw/ps2204/index.html)
(http://www.cisco.com/en/US/products/sw/opticsw/ps2204/index.html)  
http://cisco.com/go/hum =\> [CiscoWorks Health and Utilization Monitor -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9303/index.html)
(http://www.cisco.com/en/US/products/ps9303/index.html)  
http://cisco.com/go/pvm =\> [Cisco Performance Visibility Manager -
Network Performance - Products & Services - Cisco Systems - Cisco
Systems](http://www.cisco.com/en/US/products/ps6768/index.html)
(http://www.cisco.com/en/US/products/ps6768/index.html)  
http://cisco.com/go/san =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns893/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns893/networking\_solutions\_package.html)  
http://cisco.com/go/wan =\> [Unified WAN Services Platforms  [Routers] -
Cisco
Systems](http://www.cisco.com/en/US/prod/routers/networking_solutions_products_unified_wan_services_platforms.html)
(http://www.cisco.com/en/US/prod/routers/networking\_solutions\_products\_unified\_wan\_services\_platforms.html)  
http://cisco.com/go/sbn =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/security/borderless_security.html)(http://www.cisco.com/web/partners/sell/technology/security/borderless\_security.html)  
http://cisco.com/go/cdn =\> [Cisco Developer Community - Home - Cisco
Developer Community](http://developer.cisco.com)
(http://developer.cisco.com)  
http://cisco.com/go/sdn =\> [Security Solutions for Enterprise - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/cfn =\> [Cisco Feature Navigator - Cisco
Systems](http://tools.cisco.com/ITDIT/CFN/)
(http://tools.cisco.com/ITDIT/CFN/)  
http://cisco.com/go/cin =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/partners/events/cin.html)
(http://www.cisco.com/web/partners/events/cin.html)  
http://cisco.com/go/aon =\> [Application-Oriented Networking - Cisco
Systems](http://www.cisco.com/en/US/products/ps6692/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps6692/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/cpn =\> [Shortcut Redirect - Cisco
Systems](http://www.cisco.com/pcgi-bin/cpn/cpn_pub_bassrch.pl)
(http://www.cisco.com/pcgi-bin/cpn/cpn\_pub\_bassrch.pl)  
http://cisco.com/go/vpn =\> [Virtual Private Networks (VPN) - Main
Page - Cisco
Systems](http://www.cisco.com/en/US/products/ps5743/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps5743/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/brn =\> [Places in the Network - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns936/index.html)
(http://www.cisco.com/en/US/netsol/ns936/index.html)  
http://cisco.com/go/cio =\> [CIO - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns1018/index.html)
(http://www.cisco.com/en/US/netsol/ns1018/index.html)  
http://cisco.com/go/sio =\> [Security Intelligence Operations - Cisco
Systems](http://tools.cisco.com/security/center/home.x)
(http://tools.cisco.com/security/center/home.x)  
http://cisco.com/go/cpo =\>
[](https://tools.cisco.com/gdrp/coiga/showsurvey.do?surveyCode=445&keyCode=106721_1)(https://tools.cisco.com/gdrp/coiga/showsurvey.do?surveyCode=445&keyCode;=106721\_1)  
http://cisco.com/go/map =\> [401 Authorization
Required](http://www.cisco-services.com/map)
(http://www.cisco-services.com/map)  
http://cisco.com/go/sap =\> [DC Partner - SAP - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns970/index.html)
(http://www.cisco.com/en/US/netsol/ns970/index.html)  
http://cisco.com/go/tap =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/tap/index.html)(http://www.cisco.com/web/partners/pr11/incentive/tap/index.html)  
http://cisco.com/go/tbp =\> [Cisco Trusted Business
Professional](https://programs.regweb.com/cisco/ctbp_08/)
(https://programs.regweb.com/cisco/ctbp\_08/)  
http://cisco.com/go/ccp =\> [Cisco Configuration Professional - Products
& Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9422/index.html)
(http://www.cisco.com/en/US/products/ps9422/index.html)  
http://cisco.com/go/gep =\> [Global EasyPay (GEP) - Partner Central -
Cisco
Systems](http://www.cisco.com/web/partners/tools/global_easypay.html)(http://www.cisco.com/web/partners/tools/global\_easypay.html)  
http://cisco.com/go/rep =\> [Cisco.com Login
Page](http://tools.cisco.com/WWChannels/CAMLOC/jsp/cam_locator.jsp)
(http://tools.cisco.com/WWChannels/CAMLOC/jsp/cam\_locator.jsp)  
http://cisco.com/go/nfp =\> [Cisco IOS Network Foundation Protection
(NFP) - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6642/index.html)
(http://www.cisco.com/en/US/products/ps6642/index.html)  
http://cisco.com/go/agp =\> [Cisco.com Login
Page](https://tools.cisco.com/WWChannels/MBO/home.do)
(https://tools.cisco.com/WWChannels/MBO/home.do)  
http://cisco.com/go/cip =\> [Cisco Channel Interface Processors -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/modules/ps2643/ps123/index.html)
(http://www.cisco.com/en/US/products/hw/modules/ps2643/ps123/index.html)  
http://cisco.com/go/dip =\> [We Apologize - 401
Error](http://www.cisco.com/global/EMEA/pages/dip/)(http://www.cisco.com/global/EMEA/pages/dip/)  
http://cisco.com/go/sip =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/sip.html)(http://www.cisco.com/web/partners/pr11/incentive/sip.html)  
http://cisco.com/go/vip =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr11/incentive/vip.shtml)
(http://www.cisco.com/en/US/partner/partners/pr11/incentive/vip.shtml)  
http://cisco.com/go/oip =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr11/incentive/oip.shtml)
(http://www.cisco.com/en/US/partner/partners/pr11/incentive/oip.shtml)  
http://cisco.com/go/sjp =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/sip.html)(http://www.cisco.com/web/partners/pr11/incentive/sip.html)  
http://cisco.com/go/dlp =\> [Data Loss Prevention - Cisco
Systems](http://cisco.com/en/US/netsol/ns895/index.html)
(http://cisco.com/en/US/netsol/ns895/index.html)  
http://cisco.com/go/clp =\> [Cisco Learning Partner - Learning Partners
Program Overview - Cisco
Systems](http://www.cisco.com/web/learning/le27/le53/learning_partner_clp.html)(http://www.cisco.com/web/learning/le27/le53/learning\_partner\_clp.html)  
http://cisco.com/go/dmp =\> [Cisco.com Login
Page](http://tools.cisco.com/emea/dmt/index.jsp)
(http://tools.cisco.com/emea/dmt/index.jsp)  
http://cisco.com/go/cpp =\> [Cisco Powered Program for the Service
Provider - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns851/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns851/networking\_solutions\_solution.html)  
http://cisco.com/go/dpp =\> [Cisco.com Login
Page](https://tools.cisco.com/WWChannels/MBO/home.do)
(https://tools.cisco.com/WWChannels/MBO/home.do)  
http://cisco.com/go/app =\> [Other Cisco Programs - Partner Central -
Cisco
Systems](http://www.cisco.com/en/US/partners/pr46/partners_pgm_category_page.html)(http://www.cisco.com/en/US/partners/pr46/partners\_pgm\_category\_page.html)  
http://cisco.com/go/urp =\> [Redirect Notification - This page has moved
to a new location! - Cisco
Systems](http://www.cisco.com/web/about/ac50/ac207/crc/index1.html)(http://www.cisco.com/web/about/ac50/ac207/crc/index1.html)  
http://cisco.com/go/asp =\>
[Log-In](http://resources.cisco.com/app/tree.taf?asset_id=482157&public_view=true)
(http://resources.cisco.com/app/tree.taf?asset\_id=482157&public;\_view=true)  
http://cisco.com/go/ksp =\> [Knowledge Services - Advanced Services
Education - Cisco
Systems](http://www.cisco.com/web/learning/le31/ase/knowledgeservices/index.html)(http://www.cisco.com/web/learning/le31/ase/knowledgeservices/index.html)  
http://cisco.com/go/psp =\> [Public Sector Program (PSP) - Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/em/em_psp.html)(http://www.cisco.com/web/partners/pr11/incentive/em/em\_psp.html)  
http://cisco.com/go/atp =\> [Authorized Technology Provider (ATP)
Program - Partner Central - Cisco
Systems](http://www.cisco.com/web/partners/pr11/atp/index.html)(http://www.cisco.com/web/partners/pr11/atp/index.html)  
http://cisco.com/go/cvp =\> [Cisco Unified Customer Voice Portal -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/custcosw/ps1006/index.html)
(http://www.cisco.com/en/US/products/sw/custcosw/ps1006/index.html)  
http://cisco.com/go/axp =\> [Optimize Branch Footprint with Application
Integration   [Cisco Application Extension Platform] - Cisco
Systems](http://www.cisco.com/en/US/prod/routers/ps9701/axp_promo.html)
(http://www.cisco.com/en/US/prod/routers/ps9701/axp\_promo.html)  
http://cisco.com/go/p4p =\> [Cisco
Systems](http://www.cisco.com/web/partners/services/promos/p4p/index.html)(http://www.cisco.com/web/partners/services/promos/p4p/index.html)  
http://cisco.com/go/sbr =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/smb/tools_and_resources/smart_business_roadmap.html)(http://www.cisco.com/web/partners/sell/smb/tools\_and\_resources/smart\_business\_roadmap.html)  
http://cisco.com/go/pdr =\> [Cisco.com Login
Page](https://cisco-apps.cisco.com/cisco/psn/commerce)
(https://cisco-apps.cisco.com/cisco/psn/commerce)  
http://cisco.com/go/oer =\> [Cisco Optimized Edge Routing - Cisco
Systems](http://www.cisco.com/en/US/products/ps6628/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps6628/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/pfr =\> [Performance Routing - Cisco
Systems](http://www.cisco.com/en/US/products/ps8787/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps8787/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/ehr =\> [502 Proxy
Error](http://www.cisco.com/web/strategy/healthcare/breathe_life_into_ehr.html)
(http://www.cisco.com/web/strategy/healthcare/breathe\_life\_into\_ehr.html)  
http://cisco.com/go/air =\> [Airports - Transportation - Cisco
Systems](http://www.cisco.com/en/US/strategy/transportation/airports.html)(http://www.cisco.com/en/US/strategy/transportation/airports.html)  
http://cisco.com/go/asr =\> [Introducing the Cisco ASR 1000 Router
Series  [Cisco ASR 1000 Series Aggregation Services Routers] - Cisco
Systems](http://www.cisco.com/en/US/prod/routers/ps9343/asr_1000_prod_announcement.html)
(http://www.cisco.com/en/US/prod/routers/ps9343/asr\_1000\_prod\_announcement.html)  
http://cisco.com/go/abs =\>
[](http://www.crmtool.net/WebForm.asp?F=251&W=2824)(http://www.crmtool.net/WebForm.asp?F=251&W;=2824)  
http://cisco.com/go/cbs =\> [WebEx Helps Crack The Case On CSI: Miami -
Video Detail - The Video
Lounge](http://videolounge.cisco.com/video/csi-miami-webex-cracks-case/?Referring_site=PrintTv&Country_Site=US&Campaign=HN&Position=URL&Creative=go/cbs&Where=go/cbs)
(http://videolounge.cisco.com/video/csi-miami-webex-cracks-case/?Referring\_site=PrintTv&Country;\_Site=US&Campaign;=HN&Position;=URL&Creative;=go/cbs&Where;=go/cbs)  
http://cisco.com/go/acs =\> [Cisco Secure Access Control System - Cisco
Systems](http://cisco.com/en/US/products/ps9911/index.html)
(http://cisco.com/en/US/products/ps9911/index.html)  
http://cisco.com/go/ics =\> [Cisco Incident Control System - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6542/index.html)
(http://www.cisco.com/en/US/products/ps6542/index.html)  
http://cisco.com/go/scs =\> [Secure Remote Access and VPN - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns461/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns461/networking\_solutions\_package.html)  
http://cisco.com/go/cds =\> [Content Delivery Systems - Cisco
Systems](http://www.cisco.com/en/US/products/ps7191/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps7191/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/ids =\> [Shortcut Redirect - Cisco
Systems](http://www.cisco.com/go/ips) (http://www.cisco.com/go/ips)  
http://cisco.com/go/tds =\> [Threat Control - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/ns441/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/ns441/networking\_solutions\_package.html)  
http://cisco.com/go/ams =\> [Cisco Assurance Management Solution -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps8408/index.html)
(http://www.cisco.com/en/US/products/ps8408/index.html)  
http://cisco.com/go/dms =\> [Digital Media Suite - Cisco
Systems](http://www.cisco.com/web/solutions/dms/)(http://www.cisco.com/web/solutions/dms/)  
http://cisco.com/go/nms =\> [Network Management - Main Page - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)  
http://cisco.com/go/sms =\> [Text Messaging at Cisco - About Cisco -
Cisco
Systems](http://www.cisco.com/web/about/facts_info/sms_reg_info.html)(http://www.cisco.com/web/about/facts\_info/sms\_reg\_info.html)  
http://cisco.com/go/ans =\> [Application Networking Services - Main
Page - Cisco
Systems](http://www.cisco.com/en/US/products/hw/contnetw/index.html)
(http://www.cisco.com/en/US/products/hw/contnetw/index.html)  
http://cisco.com/go/dns =\> [Dynamic Host Control Protocol (DHCP)/Domain
Name System (DNS) - Cisco
Systems](http://www.cisco.com/en/US/products/ps6641/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps6641/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/eos =\> [Cisco Certified Refurbished Equipment -
Cisco Capital Finance - Cisco
Systems](http://www.cisco.com/web/ordering/ciscocapital/refurbished/index.html)(http://www.cisco.com/web/ordering/ciscocapital/refurbished/index.html)  
http://cisco.com/go/ios =\> [Cisco IOS and NX-OS Software - Main Page -
Cisco
Systems](http://www.cisco.com/en/US/products/sw/iosswrel/products_ios_cisco_ios_software_category_home.html)
(http://www.cisco.com/en/US/products/sw/iosswrel/products\_ios\_cisco\_ios\_software\_category\_home.html)  
http://cisco.com/go/qos =\> [Quality of Service (QoS) - Cisco
Systems](http://www.cisco.com/en/US/products/ps6558/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6558/products\_ios\_technology\_home.html)  
http://cisco.com/go/ros =\> [Remote Management Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6192/serv_category_home.html)
(http://www.cisco.com/en/US/products/ps6192/serv\_category\_home.html)  
http://cisco.com/go/wos =\> [Overview - Exhibit & Sponsorship
Opportunities - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/networkers/nw07/wos)(http://www.cisco.com/web/learning/le21/le34/networkers/nw07/wos)  
http://cisco.com/go/ips =\> [Cisco Intrusion Prevention System -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/secursw/ps2113/index.html)
(http://www.cisco.com/en/US/products/sw/secursw/ps2113/index.html)  
http://cisco.com/go/ops =\> [Cisco.com Login
Page](http://www.cisco.com/cgi-bin/cpn/show_page.pl?file_name=symposiums.html&type=technical)
(http://www.cisco.com/cgi-bin/cpn/show\_page.pl?file\_name=symposiums.html&type;=technical)  
http://cisco.com/go/crs =\> [Cisco Carrier Routing System - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5763/index.html)
(http://www.cisco.com/en/US/products/ps5763/index.html)  
http://cisco.com/go/oss =\> [Network Management - Main Page - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)  
http://cisco.com/go/pss =\> [Cisco.com Login
Page](http://tools.cisco.com/WWChannels/GETLOG/welcome.do)
(http://tools.cisco.com/WWChannels/GETLOG/welcome.do)  
http://cisco.com/go/tss =\> [Technical Services - Cisco
Systems](http://www.cisco.com/en/US/products/svcs/ps3034/serv_category_home.html)
(http://www.cisco.com/en/US/products/svcs/ps3034/serv\_category\_home.html)  
http://cisco.com/go/vss =\> [Cisco Catalyst 6500 Virtual Switching
System 1440 - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9336/index.html)
(http://www.cisco.com/en/US/products/ps9336/index.html)  
http://cisco.com/go/fts =\> [Cisco Focused Technical Support Services -
Cisco
Systems](http://www.cisco.com/en/US/products/svcs/ps11/ps2566/ps2567/serv_group_home.html)
(http://www.cisco.com/en/US/products/svcs/ps11/ps2566/ps2567/serv\_group\_home.html)  
http://cisco.com/go/avs =\> [Cisco AVS 3100 Series Application Velocity
System - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6492/index.html)
(http://www.cisco.com/en/US/products/ps6492/index.html)  
http://cisco.com/go/uws =\> [Unified WAN Services - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns780/index.html)
(http://www.cisco.com/en/US/netsol/ns780/index.html)  
http://cisco.com/go/act =\> [Cisco Systems, Inc](http://www.cisco.com)
(http://www.cisco.com)  
http://cisco.com/go/ect =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns855/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns855/networking\_solutions\_package.html)  
http://cisco.com/go/hft =\> [HFT: Algo Speed - Financial Markets -
Financial Markets - Cisco
Systems](http://www.cisco.com/web/strategy/financial/algo_speed.html)(http://www.cisco.com/web/strategy/financial/algo\_speed.html)  
http://cisco.com/go/pit =\> [Cisco.com Login
Page](http://tools.cisco.com/Support/CPI/index.do)
(http://tools.cisco.com/Support/CPI/index.do)  
http://cisco.com/go/int =\> [í+µíc í.Oí\_¬ë+\_ë¡oì\_ - ì\`ì+Oê,°ì-.
ì+"ë£"ì.\~ - Cisco
Systems](http://www.cisco.com/web/KR/networking/smbiz/integrated_tech.html)(http://www.cisco.com/web/KR/networking/smbiz/integrated\_tech.html)  
http://cisco.com/go/ipt =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/ns268/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns165/ns268/networking\_solutions\_package.html)  
http://cisco.com/go/prt =\> [Partner Relationship Team - Cisco
Systems](http://tools.cisco.com/elearning/knet/faq/jsp/faqcontroller.jsp?action=faqList&type=0:1&module=FAQ&appid=11625&rootcatid=11625&targetID=11625)
(http://tools.cisco.com/elearning/knet/faq/jsp/faqcontroller.jsp?action=faqList&type;=0:1&module;=FAQ&appid;=11625&rootcatid;=11625&targetID;=11625)  
http://cisco.com/go/fst =\> [Financial Services - Industry Solutions -
Cisco
Systems](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/att =\> [Cisco - AT&T; UP - Thank
You](https://programs.regweb.com/cisco/stayingoncourse_thankyou/)
(https://programs.regweb.com/cisco/stayingoncourse\_thankyou/)  
http://cisco.com/go/ett =\>
[Log-In](http://resources.cisco.com/app/tree.taf?asset_id=126014&public_view=true&LeftNavID=142323)
(http://resources.cisco.com/app/tree.taf?asset\_id=126014&public;\_view=true&LeftNavID;=142323)  
http://cisco.com/go/ftt =\> [Fast Track Trade
In](http://tools.cisco.com/WWChannels/MBO/FTT/home.html)
(http://tools.cisco.com/WWChannels/MBO/FTT/home.html)  
http://cisco.com/go/rtt =\>
[Log-In](http://resources.cisco.com/app/tree.taf?asset_id=136369&public_view=true&randomid=0.1&LeftNavID=136369)
(http://resources.cisco.com/app/tree.taf?asset\_id=136369&public;\_view=true&randomid;=0.1&LeftNavID;=136369)  
http://cisco.com/go/evt =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/ipc/announcements/evt_roadshow.html)(http://www.cisco.com/web/partners/sell/technology/ipc/announcements/evt\_roadshow.html)  
http://cisco.com/go/pvt =\> [Cisco Partner Virtual Team
Events](https://programs.regweb.com/cisco/pvt_08/)
(https://programs.regweb.com/cisco/pvt\_08/)  
http://cisco.com/go/cnu =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr46/cnu/index.html)(http://www.cisco.com/web/partners/pr46/cnu/index.html)  
http://cisco.com/go/gov =\> [e-government - U.S. Federal
Government -Industry Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/government/us_federal.html)(http://www.cisco.com/web/strategy/government/us\_federal.html)  
http://cisco.com/go/cpv =\> [Cisco.com Login
Page](http://tools.cisco.com/Support/mytechsupport/index.jsp)
(http://tools.cisco.com/Support/mytechsupport/index.jsp)  
http://cisco.com/go/pgw =\> [Cisco PGW 2200 Softswitch - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/vcallcon/ps2027/index.html)
(http://www.cisco.com/en/US/products/hw/vcallcon/ps2027/index.html)  
http://cisco.com/go/fax =\> [Cisco Fax Server - Products & Services -
Cisco Systems](http://www.cisco.com/en/US/products/ps6178/index.html)
(http://www.cisco.com/en/US/products/ps6178/index.html)  
http://cisco.com/go/ccx =\> [Cisco Compatible Extensions Client
Devices - Cisco Compatible Extensions - Cisco
Systems](http://www.cisco.com/web/partners/pr46/pr147/partners_pgm_partners_0900aecd800a7907.html)(http://www.cisco.com/web/partners/pr46/pr147/partners\_pgm\_partners\_0900aecd800a7907.html)  
http://cisco.com/go/fox =\> [President Taylor Meets Over TelePresence On
24 - Video Detail - The Video
Lounge](http://videolounge.cisco.com/video/24-pres-taylor-meets-over-tp/?Referring_site=PrintTv&Country_Site=US&Campaign=HN&Position=URL&Creative=go/fox&Where=go/fox)
(http://videolounge.cisco.com/video/24-pres-taylor-meets-over-tp/?Referring\_site=PrintTv&Country;\_Site=US&Campaign;=HN&Position;=URL&Creative;=go/fox&Where;=go/fox)  
http://cisco.com/go/biz =\> [Internal Server
Error](http://www.cisco.com/cisco/web/solutions/small_business/index.html?Referring_site=PrintTv&Country_Site=us&Campaign=SAMBA&Position=Vanity&Creative=go/biz&Where=go/biz)
(http://www.cisco.com/cisco/web/solutions/small\_business/index.html?Referring\_site=PrintTv&Country;\_Site=us&Campaign;=SAMBA&Position;=Vanity&Creative;=go/biz&Where;=go/biz)  
http://cisco.com/go/100 =\> [Cisco SB 100 Series Small-Business
Routers - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6216/index.html)
(http://www.cisco.com/en/US/products/ps6216/index.html)  
http://cisco.com/go/850 =\> [Cisco 851 Integrated Services Router -
Cisco Systems](http://www.cisco.com/en/US/products/ps6195/index.html)
(http://www.cisco.com/en/US/products/ps6195/index.html)  
http://cisco.com/go/360 =\> [\> Cisco 360 Learning Program - The Cisco
Learning
Network](https://learningnetwork.cisco.com/community/learning_center/cisco_360)
(https://learningnetwork.cisco.com/community/learning\_center/cisco\_360)  
http://cisco.com/go/870 =\> [Cisco 871 Integrated Services Router -
Cisco Systems](http://www.cisco.com/en/US/products/ps6200/index.html)
(http://www.cisco.com/en/US/products/ps6200/index.html)  
http://cisco.com/go/fs1 =\> [Financial Services - Industry Solutions -
Cisco
Systems](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/tv1 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/vc2 =\> [VoiceCon 2010 - Cisco Events - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)(http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)  
http://cisco.com/go/fs2 =\> [Financial Services - Industry Solutions -
Cisco
Systems](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/tv2 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/fs3 =\> [Financial Services - Industry Solutions -
Cisco
Systems](http://www.cisco.com/web/strategy/financial/index.html)(http://www.cisco.com/web/strategy/financial/index.html)  
http://cisco.com/go/tv3 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv4 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv5 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv6 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv7 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv8 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/tv9 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/pica =\> [Cisco.com Login
Page](http://www.cisco.com/cgi-bin/front.x/pica/welcome_2_pica.pl)
(http://www.cisco.com/cgi-bin/front.x/pica/welcome\_2\_pica.pl)  
http://cisco.com/go/cpda =\> [The Page You Have Requested Is Not
Available](http://www.cisco-powered.com/cp/auth/marketing_sales_resources/cisco_powered_demand_accelerator/)
(http://www.cisco-powered.com/cp/auth/marketing\_sales\_resources/cisco\_powered\_demand\_accelerator/)  
http://cisco.com/go/ctia =\> [CTIA Wireless 2010 - Cisco Events - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/ctia/2010/index.html)(http://www.cisco.com/web/learning/le21/le34/ctia/2010/index.html)  
http://cisco.com/go/nila =\> [News@Cisco -\> Executive
Biographies](http://newsroom.cisco.com/dlls/tln/research_studies/nila/index.html)
(http://newsroom.cisco.com/dlls/tln/research\_studies/nila/index.html)  
http://cisco.com/go/eula =\> [End User License Agreement  [Products &
Services] - Cisco
Systems](http://www.cisco.com/en/US/docs/general/warranty/English/EU1KEN_.html)
(http://www.cisco.com/en/US/docs/general/warranty/English/EU1KEN\_.html)  
http://cisco.com/go/icpa =\> [Cisco.com Login
Page](http://tools.cisco.com/WWChannels/IPA/welcome.do#)
(http://tools.cisco.com/WWChannels/IPA/welcome.do\#)  
http://cisco.com/go/vspa =\> [Cisco Catalyst 6500 Series VPN Services
Port Adapter - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9893/index.html)
(http://www.cisco.com/en/US/products/ps9893/index.html)  
http://cisco.com/go/cspa =\> [Cisco Service Path Analyzer - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9498/index.html)
(http://www.cisco.com/en/US/products/ps9498/index.html)  
http://cisco.com/go/ncta =\> [NCTA Show 2010 - Cisco Events - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/ncta/2010/index.html)(http://www.cisco.com/web/learning/le21/le34/ncta/2010/index.html)  
http://cisco.com/go/mfib =\> [IP Multicast - Cisco
Systems](http://www.cisco.com/en/US/products/ps6552/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6552/products\_ios\_technology\_home.html)  
http://cisco.com/go/bnac =\> [Cisco BioMed Network Admission Control -
Industry Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/healthcare/bioMed_nac.html)(http://www.cisco.com/web/strategy/healthcare/bioMed\_nac.html)  
http://cisco.com/go/bpac =\> [Cisco Systems: Business Policy Advisory
Council - Login](http://forums.cisco.com/eforum/servlet/BPAC?page=main)
(http://forums.cisco.com/eforum/servlet/BPAC?page=main)  
http://cisco.com/go/cabc =\> [Cisco Hardware Inspection and Software
Re-Licensing Program  [Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/prod/hw_sw_relicensing_program.html#~using)
(http://www.cisco.com/en/US/prod/hw\_sw\_relicensing\_program.html\#\~using)  
http://cisco.com/go/brdc =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns340/ns394/ns224/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns224/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/trec =\> [Smart+Connected Real Estate - Industry
Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/trec/index.html)(http://www.cisco.com/web/strategy/trec/index.html)  
http://cisco.com/go/psfc =\> [Cisco.com Login
Page](http://tools.cisco.com/salesit/psfc/index.jsp)
(http://tools.cisco.com/salesit/psfc/index.jsp)  
http://cisco.com/go/gbic =\> [Cisco Transceiver Modules - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/modules/ps5455/prod_module_series_home.html)
(http://www.cisco.com/en/US/products/hw/modules/ps5455/prod\_module\_series\_home.html)  
http://cisco.com/go/celc =\> [Cisco Learning Home - The Cisco Learning
Network](https://cisco.hosted.jivesoftware.com/index.jspa?ciscoHome=true)
(https://cisco.hosted.jivesoftware.com/index.jspa?ciscoHome=true)  
http://cisco.com/go/cumc =\> [Cisco Unified Mobile Communicator -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7271/index.html)
(http://www.cisco.com/en/US/products/ps7271/index.html)  
http://cisco.com/go/cepc =\> [Cisco Experience Provider
Central](http://ciscoepcentral.veplatform.com)
(http://ciscoepcentral.veplatform.com)  
http://cisco.com/go/hipc =\> [Cisco Powered
Program](http://www.cisco.com/pcgi-bin/cpn/cpn_match_result.pl?perPage=40&CurPosition=0&Direction=&ResultType=EC&search_id=873856&tab_name=findsp&SearchType=Advance&sortBy=DEFAULT)
(http://www.cisco.com/pcgi-bin/cpn/cpn\_match\_result.pl?perPage=40&CurPosition;=0&Direction;=&ResultType;=EC&search;\_id=873856&tab;\_name=findsp&SearchType;=Advance&sortBy;=DEFAULT)  
http://cisco.com/go/dcuc =\> [Data Center Unified Computing - Partner
Central - Cisco
Systems](http://www.cisco.com/web/partners/pr11/atp/dcuc/index.html)(http://www.cisco.com/web/partners/pr11/atp/dcuc/index.html)  
http://cisco.com/go/road =\> [Roadways - Transportation - Cisco
Systems](http://www.cisco.com/en/US/strategy/transportation/roadways.html)(http://www.cisco.com/en/US/strategy/transportation/roadways.html)  
http://cisco.com/go/used =\> [Cisco Hardware Inspection and Software
Re-Licensing Program  [Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/prod/hw_sw_relicensing_program.html#~using)
(http://www.cisco.com/en/US/prod/hw\_sw\_relicensing\_program.html\#\~using)  
http://cisco.com/go/grid =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns500/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns500/networking\_solutions\_package.html)  
http://cisco.com/go/gold =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr11/pr8/pr27/partners_pgm_concept_home.shtml)
(http://www.cisco.com/en/US/partner/partners/pr11/pr8/pr27/partners\_pgm\_concept\_home.shtml)  
http://cisco.com/go/ipnd =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr11/incentive/defender.shtml)
(http://www.cisco.com/en/US/partner/partners/pr11/incentive/defender.shtml)  
http://cisco.com/go/srnd =\> [Design Zone - Main Page - Cisco - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns742/networking_solutions_program_category_home.html)
(http://www.cisco.com/en/US/netsol/ns742/networking\_solutions\_program\_category\_home.html)  
http://cisco.com/go/isrd =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/about/security/security_services/ciag/research/index.html)
(http://www.cisco.com/web/about/security/security\_services/ciag/research/index.html)  
http://cisco.com/go/apae =\> [Cisco Application Performance Assurance
Engine - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9799/index.html)
(http://www.cisco.com/en/US/products/ps9799/index.html)  
http://cisco.com/go/cuae =\> [Cisco Unified Application Environment -
Cisco
Systems](http://www.cisco.com/en/US/netsol/ns738/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns738/networking\_solutions\_package.html)  
http://cisco.com/go/cmbe =\> [Cisco Unified Communications Manager
Business Edition - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps7273/index.html)
(http://www.cisco.com/en/US/products/ps7273/index.html)  
http://cisco.com/go/cube =\> [Cisco Unified Border Element (CUBE) -
Cisco
Systems](http://www.cisco.com/en/US/products/sw/voicesw/ps5640/index.html)
(http://www.cisco.com/en/US/products/sw/voicesw/ps5640/index.html)  
http://cisco.com/go/pace =\> [Compliance - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns661/index.html)
(http://www.cisco.com/en/US/netsol/ns661/index.html)  
http://cisco.com/go/ccde =\> [502 Proxy
Error](http://www.cisco.com/web/learning/le3/ccde/index.html)
(http://www.cisco.com/web/learning/le3/ccde/index.html)  
http://cisco.com/go/edge =\> [Edge Networks - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns592/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns592/networking\_solutions\_solution.html)  
http://cisco.com/go/ccie =\> [Cisco Certified Internetwork Expert -
CCIE - Cisco
Systems](http://www.cisco.com/web/learning/le3/ccie/index.html)(http://www.cisco.com/web/learning/le3/ccie/index.html)  
http://cisco.com/go/ccme =\> [Cisco Unified Communications Manager
Express(CME) - Cisco
Systems](http://www.cisco.com/en/US/products/sw/voicesw/ps4625/index.html)
(http://www.cisco.com/en/US/products/sw/voicesw/ps4625/index.html)  
http://cisco.com/go/hire =\> [IT Managers - The Cisco Learning
Network](https://cisco.hosted.jivesoftware.com/community/promo-014-hire?utm_source=tm&utm_medium=pm&utm_campaign=promo-014)
(https://cisco.hosted.jivesoftware.com/community/promo-014-hire?utm\_source=tm&utm;\_medium=pm&utm;\_campaign=promo-014)  
http://cisco.com/go/core =\> [Core Networks - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns573/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns573/networking\_solutions\_solution.html)  
http://cisco.com/go/ahse =\> [Cisco Application-Oriented Networking
Healthcare Services Extensions - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9715/index.html)
(http://www.cisco.com/en/US/products/ps9715/index.html)  
http://cisco.com/go/ctwe =\> [Cisco TelePresence WebEx Engage 
[TelePresence] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns669/webex_engage.html)
(http://www.cisco.com/en/US/solutions/ns669/webex\_engage.html)  
http://cisco.com/go/skye =\> [Small Business Empowered by Cisco - Cisco
Systems](http://www.cisco.com/web/solutions/smb/heroes/index.html?Referring_site=PrintTv&Country_Site=us&Campaign=SMB+Heroes&Position=Vanity&Creative=go/skye&Where=go/skye)
(http://www.cisco.com/web/solutions/smb/heroes/index.html?Referring\_site=PrintTv&Country;\_Site=us&Campaign;=SMB+Heroes&Position;=Vanity&Creative;=go/skye&Where;=go/skye)  
http://cisco.com/go/dcof =\> [The Data Center of the Future - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns708/sol_generic_dc_of_the_future.html)
(http://www.cisco.com/en/US/solutions/ns708/sol\_generic\_dc\_of\_the\_future.html)  
http://cisco.com/go/svig =\> [Introduction - Silicon Valley Impact
Grants - Cisco
Systems](http://www.cisco.com/web/about/ac48/sv_grants.html)(http://www.cisco.com/web/about/ac48/sv\_grants.html)  
http://cisco.com/go/fclg =\> [Search Seminars and Webcasts - Events,
Webcasts and Seminars - Cisco
Systems](http://www.cisco.com/pcgi-bin/sreg2/register/regdetail_private.pl?LANGUAGE=E&METHOD=E&TOPIC_CODE=9947&PRIORITY_CODE=176571_4)(http://www.cisco.com/pcgi-bin/sreg2/register/regdetail\_private.pl?LANGUAGE=E&METHOD;=E&TOPIC;\_CODE=9947&PRIORITY;\_CODE=176571\_4)  
http://cisco.com/go/blog =\> [Architectures and
Solutions](http://blogs.cisco.com/ciscotalk/solutions)
(http://blogs.cisco.com/ciscotalk/solutions)  
http://cisco.com/go/ibsg =\> [Welcome to Cisco IBSG - Internet Business
Solutions Group - Cisco
Systems](http://www.cisco.com/web/about/ac79/index.html)(http://www.cisco.com/web/about/ac79/index.html)  
http://cisco.com/go/gdsg =\> [Defense - Government - Cisco
Systems](http://www.cisco.com/en/US/strategy/government/defense.html)(http://www.cisco.com/en/US/strategy/government/defense.html)  
http://cisco.com/go/ggsg =\> [Defense - Government - Cisco
Systems](http://www.cisco.com/web/strategy/government/defense.html)(http://www.cisco.com/web/strategy/government/defense.html)  
http://cisco.com/go/nmtg =\> [Network Management - Main Page - Cisco
Systems](http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)
(http://www.cisco.com/en/US/products/sw/netmgtsw/index.html)  
http://cisco.com/go/tech =\> [Cisco IOS Technologies - Cisco
Systems](http://www.cisco.com/en/US/products/ps6537/products_ios_sub_category_home.html)
(http://www.cisco.com/en/US/products/ps6537/products\_ios\_sub\_category\_home.html)  
http://cisco.com/go/dcni =\> [Advanced Data Center Networking
Infrastructure - Partner Central - Cisco
Systems](http://www.cisco.com/web/partners/program/specializations/datacenter/dcni/index.html)(http://www.cisco.com/web/partners/program/specializations/datacenter/dcni/index.html)  
http://cisco.com/go/bank =\> [This Content Has Moved - Cisco
Systems](http://www.cisco.com/now/bank) (http://www.cisco.com/now/bank)  
http://cisco.com/go/deal =\> [Cisco.com Login
Page](http://www.cisco.com/cgi-bin/front.x/AppTool/controller.cgi)
(http://www.cisco.com/cgi-bin/front.x/AppTool/controller.cgi)  
http://cisco.com/go/rail =\> [Public Transportation - Transportation -
Cisco
Systems](http://www.cisco.com/en/US/strategy/transportation/rail.html)(http://www.cisco.com/en/US/strategy/transportation/rail.html)  
http://cisco.com/go/cell =\> [Text Messaging at Cisco - About Cisco -
Cisco
Systems](http://www.cisco.com/web/about/facts_info/sms_reg_info.html)(http://www.cisco.com/web/about/facts\_info/sms\_reg\_info.html)  
http://cisco.com/go/sell =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/index.html)(http://www.cisco.com/web/partners/sell/index.html)  
http://cisco.com/go/cuwl =\> [Cisco Unified Workspace Licensing -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9156/index.html)
(http://www.cisco.com/en/US/products/ps9156/index.html)  
http://cisco.com/go/apam =\> [Cisco Application Performance Assurance
Network Module - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9559/index.html)
(http://www.cisco.com/en/US/products/ps9559/index.html)  
http://cisco.com/go/asdm =\> [Cisco Adaptive Security Device Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6121/index.html)
(http://www.cisco.com/en/US/products/ps6121/index.html)  
http://cisco.com/go/cvdm =\> [CiscoWorks CiscoView - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/cscowork/ps4565/index.html)
(http://www.cisco.com/en/US/products/sw/cscowork/ps4565/index.html)  
http://cisco.com/go/cwdm =\> [Cisco CWDM Transceiver Modules - Products
& Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6575/index.html)
(http://www.cisco.com/en/US/products/ps6575/index.html)  
http://cisco.com/go/dcnm =\> [Cisco Data Center Network Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9369/index.html)
(http://www.cisco.com/en/US/products/ps9369/index.html)  
http://cisco.com/go/tpnm =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/products/ps9800/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps9800/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/cuom =\> [Cisco Unified Operations Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6535/index.html)
(http://www.cisco.com/en/US/products/ps6535/index.html)  
http://cisco.com/go/cepm =\> [Cisco Policy Management - Cisco
Systems](http://www.cisco.com/en/US/products/ps9519/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps9519/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/cupm =\> [Provisioning - Cisco - Cisco
Systems](http://www.cisco.com/en/US/products/ps7125/index.html)
(http://www.cisco.com/en/US/products/ps7125/index.html)  
http://cisco.com/go/wism =\> [Cisco Catalyst 6500 Series/7600 Series
Wireless Services Module (WiSM) - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6526/index.html)
(http://www.cisco.com/en/US/products/ps6526/index.html)  
http://cisco.com/go/cusm =\> [Cisco Unified Service Monitor - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6536/index.html)
(http://www.cisco.com/en/US/products/ps6536/index.html)  
http://cisco.com/go/fwsm =\> [Cisco Catalyst 6500 Series Firewall
Services Module - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/modules/ps2706/ps4452/index.html)
(http://www.cisco.com/en/US/products/hw/modules/ps2706/ps4452/index.html)  
http://cisco.com/go/mwtm =\> [Cisco Mobile Wireless Transport Manager -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6472/)
(http://www.cisco.com/en/US/products/ps6472/)  
http://cisco.com/go/aibn =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/partners/pr67/pr29/aibn/solution_home.html)
(http://www.cisco.com/en/US/partners/pr67/pr29/aibn/solution\_home.html)  
http://cisco.com/go/edcn =\> [Cisco Support Community: Cisco Support
Community](http://forums.cisco.com/eforum/servlet/NetProf;jsessionid=k6x5lkj7q1.SJ2B?page=netprof&CommCmd=MB%3Fcmd%3Ddisplay_messages%26mode%3Dnew%26location%3D.ee71a00)
(http://forums.cisco.com/eforum/servlet/NetProf;jsessionid=k6x5lkj7q1.SJ2B?page=netprof&CommCmd;=MB%3Fcmd%3Ddisplay\_messages%26mode%3Dnew%26location%3D.ee71a00)  
http://cisco.com/go/ibpn =\> [Cisco Systems, Inc](http://www.cisco.com)
(http://www.cisco.com)  
http://cisco.com/go/ispn =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/industry/index.html)(http://www.cisco.com/web/partners/sell/industry/index.html)  
http://cisco.com/go/evpn =\> [Security Solutions for Enterprise - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/networking_solutions_packages_list.html)
(http://www.cisco.com/en/US/netsol/ns340/ns394/ns171/networking\_solutions\_packages\_list.html)  
http://cisco.com/go/mvpn =\> [Multicast VPN - Cisco
Systems](http://www.cisco.com/en/US/products/ps6651/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps6651/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/dcsn =\> [Advanced Data Center Storage Networking -
Partner Central - Cisco
Systems](http://www.cisco.com/web/partners/program/specializations/datacenter/dcsn/index.html)(http://www.cisco.com/web/partners/program/specializations/datacenter/dcsn/index.html)  
http://cisco.com/go/ggsn =\> [Cisco Gateway GPRS Support Node - Products
& Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/wirelssw/ps873/index.html)
(http://www.cisco.com/en/US/products/sw/wirelssw/ps873/index.html)  
http://cisco.com/go/goco =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/collaboration/gocollaborate.html)(http://www.cisco.com/web/partners/sell/technology/collaboration/gocollaborate.html)  
http://cisco.com/go/logo =\> [Cisco Brand Center - Doing Business With
Cisco - Cisco
Systems](http://www.cisco.com/en/US/about/ac50/ac47/about_cisco_brand_center.html)(http://www.cisco.com/en/US/about/ac50/ac47/about\_cisco\_brand\_center.html)  
http://cisco.com/go/demo =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/ipc/integrated-solutions/dmr.html)(http://www.cisco.com/web/partners/sell/technology/ipc/integrated-solutions/dmr.html)  
http://cisco.com/go/cspo =\> [Security Programs - Security Center -
Cisco
Systems](http://www.cisco.com/web/about/security/cspo/index.html)(http://www.cisco.com/web/about/security/cspo/index.html)  
http://cisco.com/go/pvso =\> [We Apologize - 401
Error](http://www.cisco.com/partner/services/pvso/)(http://www.cisco.com/partner/services/pvso/)  
http://cisco.com/go/dcap =\> [Data Center Assurance Program - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns758/networking_solutions_sub_program_home.html)
(http://www.cisco.com/en/US/netsol/ns758/networking\_solutions\_sub\_program\_home.html)  
http://cisco.com/go/asap =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/partners/pr192/sp_asap.html)
(http://www.cisco.com/web/partners/pr192/sp\_asap.html)  
http://cisco.com/go/csbp =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns671/networking_solutions_package.html)
(http://www.cisco.com/en/US/netsol/ns671/networking\_solutions\_package.html)  
http://cisco.com/go/dhcp =\> [Dynamic Host Control Protocol
(DHCP)/Domain Name System (DNS) - Cisco
Systems](http://www.cisco.com/en/US/products/ps6641/products_ios_protocol_option_home.html)
(http://www.cisco.com/en/US/products/ps6641/products\_ios\_protocol\_option\_home.html)  
http://cisco.com/go/mscp =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/mscp/index.html)(http://www.cisco.com/web/partners/pr11/mscp/index.html)  
http://cisco.com/go/oscp =\> [Outsourcing Channel Program - Partner
Central - Cisco
Systems](http://www.cisco.com/web/partners/pr11/outsourcing/index.html)(http://www.cisco.com/web/partners/pr11/outsourcing/index.html)  
http://cisco.com/go/mldp =\> [IP Multicast - Cisco
Systems](http://www.cisco.com/en/US/products/ps6552/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6552/products\_ios\_technology\_home.html)  
http://cisco.com/go/ctdp =\> [Introduction - Cisco Technology Developer
Program - Cisco
Systems](http://www.cisco.com/en/US/partners/pr46/tdp/index.shtml)(http://www.cisco.com/en/US/partners/pr46/tdp/index.shtml)  
http://cisco.com/go/bbip =\> [CCO Decommission
Page](http://www.cisco.com/warp/public/732/bbip/)
(http://www.cisco.com/warp/public/732/bbip/)  
http://cisco.com/go/clip =\> [Cisco
Systems](http://www.cisco.com/web/ordering/ciscocapital/o45/ordering_finance_solution_program0900aecd800ddd5f.html)(http://www.cisco.com/web/ordering/ciscocapital/o45/ordering\_finance\_solution\_program0900aecd800ddd5f.html)  
http://cisco.com/go/grip =\> [High Availability - Cisco
Systems](http://www.cisco.com/en/US/products/ps6550/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6550/products\_ios\_technology\_home.html)  
http://cisco.com/go/ctmp =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/tmp/index.html)(http://www.cisco.com/web/partners/pr11/incentive/tmp/index.html)  
http://cisco.com/go/coop =\> [Cisco Coop Fund
Builder](http://www.coams.com/ciscocoop)
(http://www.coams.com/ciscocoop)  
http://cisco.com/go/mtop =\> [Radio Access Networks - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns675/networking_solutions_solution_category.html)
(http://www.cisco.com/en/US/netsol/ns675/networking\_solutions\_solution\_category.html)  
http://cisco.com/go/clsp =\> [Cisco Learning Solutions Partner -
Learning Partners Program Overview - Cisco
Systems](http://www.cisco.com/web/learning/le27/le53/learning_partner_clsp.html)(http://www.cisco.com/web/learning/le27/le53/learning\_partner\_clsp.html)  
http://cisco.com/go/cusp =\> [Cisco Unified SIP Proxy - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps10140/index.html)
(http://www.cisco.com/en/US/products/ps10140/index.html)  
http://cisco.com/go/cptp =\> [Cisco Partner Talent
Network](https://secure.partnertalentportal.com/emerging/admin9021/login.asp)
(https://secure.partnertalentportal.com/emerging/admin9021/login.asp)  
http://cisco.com/go/ccvp =\> [CCVP - Career Certifications & Paths -
Cisco
Systems](http://www.cisco.com/en/US/learning/le3/le2/le37/le65/learning_certification_type_home.html)(http://www.cisco.com/en/US/learning/le3/le2/le37/le65/learning\_certification\_type\_home.html)  
http://cisco.com/go/rsvp =\> [Cisco RSVP Agent - Products & Services -
Cisco Systems](http://www.cisco.com/en/US/products/ps6832/index.html)
(http://www.cisco.com/en/US/products/ps6832/index.html)  
http://cisco.com/go/nbar =\> [Network Based Application Recognition
(NBAR) - Cisco
Systems](http://www.cisco.com/en/US/products/ps6616/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6616/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/eccr =\> [Experience Cisco Collaboration Roadshow -
Cisco Unified Communications & WebEx - Cisco
Systems](http://www.cisco.com/web/partners/sell/technology/ipc/announcements/uc7roadshow.html)(http://www.cisco.com/web/partners/sell/technology/ipc/announcements/uc7roadshow.html)  
http://cisco.com/go/dcdr =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/euro/dcdr.html)(http://www.cisco.com/web/partners/pr11/incentive/euro/dcdr.html)  
http://cisco.com/go/iaas =\> [Infrastructure as a Service - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns995/networking_solutions_solution_category.html)
(http://www.cisco.com/en/US/netsol/ns995/networking\_solutions\_solution\_category.html)  
http://cisco.com/go/waas =\> [WAN Optimization - Cisco
Systems](http://www.cisco.com/en/US/products/ps5680/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps5680/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/dcas =\> [Data Center Application Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5719/Products_Sub_Category_Home.html)
(http://www.cisco.com/en/US/products/ps5719/Products\_Sub\_Category\_Home.html)  
http://cisco.com/go/cabs =\> [Cisco.com Login
Page](http://forums.cisco.com/eforum/servlet/CAB?page=main&sn=CAB)
(http://forums.cisco.com/eforum/servlet/CAB?page=main&sn;=CAB)  
http://cisco.com/go/mibs =\> [Cisco IOS MIB
Locator](http://tools.cisco.com/ITDIT/MIBS/servlet/index)
(http://tools.cisco.com/ITDIT/MIBS/servlet/index)  
http://cisco.com/go/isbs =\> [Design Zone for Branch - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns816/networking_solutions_program_home.html)
(http://www.cisco.com/en/US/netsol/ns816/networking\_solutions\_program\_home.html)  
http://cisco.com/go/sbcs =\> [Cisco Smart Business Communications
System - Cisco
Systems](http://www.cisco.com/cisco/web/solutions/small_business/products/voice_conferencing/smart_business_communications_system/index.html?Referring_site=PrintTv&Country_Site=us&Campaign=SAMBA&Position=Vanity&Creative=go/sbcs&Where=go/sbcs)(http://www.cisco.com/cisco/web/solutions/small\_business/products/voice\_conferencing/smart\_business\_communications\_system/index.html?Referring\_site=PrintTv&Country;\_Site=us&Campaign;=SAMBA&Position;=Vanity&Creative;=go/sbcs&Where;=go/sbcs)  
http://cisco.com/go/hucs =\> [Cisco Hosted Unified Communications
Services - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns757/networking_solutions_solution.html)
(http://www.cisco.com/en/US/netsol/ns757/networking\_solutions\_solution.html)  
http://cisco.com/go/wids =\> [Cisco Adaptive Wireless IPS Software -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9817/index.html)
(http://www.cisco.com/en/US/products/ps9817/index.html)  
http://cisco.com/go/bugs =\> [Cisco.com Login
Page](http://tools.cisco.com/Support/BugToolKit/action.do?hdnAction=searchBugs)
(http://tools.cisco.com/Support/BugToolKit/action.do?hdnAction=searchBugs)  
http://cisco.com/go/iris =\> [Cisco Internet Routing in Space (IRIS) -
Industry Solutions - Cisco
Systems](http://www.cisco.com/web/strategy/government/space-routing.html)(http://www.cisco.com/web/strategy/government/space-routing.html)  
http://cisco.com/go/mpls =\> [Multiprotocol Label Switching (MPLS) -
Cisco
Systems](http://www.cisco.com/en/US/products/ps6557/products_ios_technology_home.html)
(http://www.cisco.com/en/US/products/ps6557/products\_ios\_technology\_home.html)  
http://cisco.com/go/vams =\> [Cisco Video Assurance Management
Solution - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9518/index.html)
(http://www.cisco.com/en/US/products/ps9518/index.html)  
http://cisco.com/go/cpms =\> [Welcome - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/cpnmarketing/2007/)(http://www.cisco.com/web/learning/le21/le34/cpnmarketing/2007/)  
http://cisco.com/go/lpms =\> [Cisco.com Login
Page](http://tools.cisco.com/E-Learning-IT/LPCM/jsp/LpcmWelcome.jsp)
(http://tools.cisco.com/E-Learning-IT/LPCM/jsp/LpcmWelcome.jsp)  
http://cisco.com/go/ibns =\> [Identity Based Networking Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6638/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps6638/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/nxos =\> [Cisco NX-OS Software - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9372/index.html)
(http://www.cisco.com/en/US/products/ps9372/index.html)  
http://cisco.com/go/nips =\> [News@Cisco -\> Executive
Biographies](http://newsroom.cisco.com/dlls/tln/research_studies/nips/index.html)
(http://newsroom.cisco.com/dlls/tln/research\_studies/nips/index.html)  
http://cisco.com/go/wips =\> [Cisco Adaptive Wireless IPS Software -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps9817/index.html)
(http://www.cisco.com/en/US/products/ps9817/index.html)  
http://cisco.com/go/apps =\> [Cisco Systems: Unified Communications
Applications
Central](http://forums.cisco.com/eforum/servlet/IPCApps?page=main)
(http://forums.cisco.com/eforum/servlet/IPCApps?page=main)  
http://cisco.com/go/mars =\> [Cisco Security Monitoring, Analysis, and
Response System (MARS) - Cisco Systems - Cisco
Systems](http://www.cisco.com/en/US/products/ps6241/index.html)
(http://www.cisco.com/en/US/products/ps6241/index.html)  
http://cisco.com/go/nbss =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns614/networking_solutions_sub_solution.html)
(http://www.cisco.com/en/US/netsol/ns614/networking\_solutions\_sub\_solution.html)  
http://cisco.com/go/ucss =\> [Cisco Unified Communications Software
Subscription (UCSS) - Cisco
Systems](http://www.cisco.com/en/US/products/ps9158/index.html)
(http://www.cisco.com/en/US/products/ps9158/index.html)  
http://cisco.com/go/gdss =\> [502 Proxy
Error](http://www.cisco.com/en/US/strategy/government/defense.html)
(http://www.cisco.com/en/US/strategy/government/defense.html)  
http://cisco.com/go/ciss =\> [Cisco Feature Navigator - Cisco
Systems](http://tools.cisco.com/ITDIT/ISTMAIN/jsp/index.jsp)
(http://tools.cisco.com/ITDIT/ISTMAIN/jsp/index.jsp)  
http://cisco.com/go/cnss =\> [07/01/03 - Recent Program Information -
Cisco
Systems](http://www.cisco.com/web/learning/le3/whats_new/infosec.html)(http://www.cisco.com/web/learning/le3/whats\_new/infosec.html)  
http://cisco.com/go/skus =\> [Cisco
Systems](http://www.cisco.com/web/partners/pr11/incentive/eligible_skus.html)(http://www.cisco.com/web/partners/pr11/incentive/eligible\_skus.html)  
http://cisco.com/go/news =\> [News@Cisco -\>
News@Cisco](http://newsroom.cisco.com/dlls/index.html)
(http://newsroom.cisco.com/dlls/index.html)  
http://cisco.com/go/csat =\> [Customer Satisfaction - Cisco
Systems](http://www.cisco.com/web/partners/pr11/pr20/partners_customer_satisfaction_concept_home.html)(http://www.cisco.com/web/partners/pr11/pr20/partners\_customer\_satisfaction\_concept\_home.html)  
http://cisco.com/go/cebt =\> [Collaboration Enabled Business
Transformation - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns952/index.html)
(http://www.cisco.com/en/US/netsol/ns952/index.html)  
http://cisco.com/go/msft =\> [DC Partner - Microsoft - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns963/index.html)
(http://www.cisco.com/en/US/netsol/ns963/index.html)  
http://cisco.com/go/lcmt =\> [Cisco.com Login
Page](http://tools.cisco.com/GET/lrncrd/jsp/index.jsp)
(http://tools.cisco.com/GET/lrncrd/jsp/index.jsp)  
http://cisco.com/go/cart =\>
[Log-In](http://resources.cisco.com/app/tree.taf?asset_id=175513&public_view=true)
(http://resources.cisco.com/app/tree.taf?asset\_id=175513&public;\_view=true)  
http://cisco.com/go/srst =\> [Cisco Unified Survivable Remote Site
Telephony - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/voicesw/ps2169/index.html)
(http://www.cisco.com/en/US/products/sw/voicesw/ps2169/index.html)  
http://cisco.com/go/issu =\> [In-Service Software Upgrade (ISSU) - Cisco
Systems](http://www.cisco.com/en/US/products/ps7149/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps7149/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/srsv =\> [Cisco Survivable Remote Site Voicemail -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps10769/index.html)
(http://www.cisco.com/en/US/products/ps10769/index.html)  
http://cisco.com/go/iptv =\> [IPTV Solutions - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns610/networking_solutions_solution_category.html)
(http://www.cisco.com/en/US/netsol/ns610/networking\_solutions\_solution\_category.html)  
http://cisco.com/go/rfgw =\> [Cisco RF Gateway Series - Products &
Services - Cisco
Systems](https://www.cisco.com/en/US/products/ps8360/index.html)
(https://www.cisco.com/en/US/products/ps8360/index.html)  
http://cisco.com/go/grow =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/web/partners/grow.html)
(http://www.cisco.com/web/partners/grow.html)  
http://cisco.com/go/cbsw =\> [Cisco
Systems](http://www.cisco.com/web/partners/sell/smb/university/training.html)(http://www.cisco.com/web/partners/sell/smb/university/training.html)  
http://cisco.com/go/uccx =\> [Cisco Unified Contact Center Express -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/sw/custcosw/ps1846/index.html)
(http://www.cisco.com/en/US/products/sw/custcosw/ps1846/index.html)  
http://cisco.com/go/amex =\> [The Page You Have Requested Is Not
Available](http://www.cisco.com/en/US/netsol/ns339/networking_solutions_small_medium_sized_business_home.html)
(http://www.cisco.com/en/US/netsol/ns339/networking\_solutions\_small\_medium\_sized\_business\_home.html)  
http://cisco.com/go/gray =\> [Cisco Hardware Inspection and Software
Re-Licensing Program  [Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/prod/hw_sw_relicensing_program.html#~using)
(http://www.cisco.com/en/US/prod/hw\_sw\_relicensing\_program.html\#\~using)  
http://cisco.com/go/grey =\> [Cisco Hardware Inspection and Software
Re-Licensing Program  [Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/prod/hw_sw_relicensing_program.html#~using)
(http://www.cisco.com/en/US/prod/hw\_sw\_relicensing\_program.html\#\~using)  
http://cisco.com/go/easy =\> [Cisco Embedded Automation Systems - Cisco
Systems](http://www.cisco.com/en/US/products/ps10777/products_ios_protocol_group_home.html)
(http://www.cisco.com/en/US/products/ps10777/products\_ios\_protocol\_group\_home.html)  
http://cisco.com/go/4200 =\> [Cisco IPS 4200 Series Sensors - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/vpndevc/ps4077/index.html)
(http://www.cisco.com/en/US/products/hw/vpndevc/ps4077/index.html)  
http://cisco.com/go/4500 =\> [Cisco Catalyst 4500 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/switches/ps4324/index.html)
(http://www.cisco.com/en/US/products/hw/switches/ps4324/index.html)  
http://cisco.com/go/6500 =\> [Cisco Catalyst 6500 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/switches/ps708/index.html)
(http://www.cisco.com/en/US/products/hw/switches/ps708/index.html)  
http://cisco.com/go/3700 =\> [Cisco -Cisco 3700 Series
Routers](http://www.cisco.com/warp/public/cc/pd/rt/ps282/)
(http://www.cisco.com/warp/public/cc/pd/rt/ps282/)  
http://cisco.com/go/3800 =\> [Cisco 3800 Series Integrated Services
Routers - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5855/index.html)
(http://www.cisco.com/en/US/products/ps5855/index.html)  
http://cisco.com/go/1800 =\> [Cisco 1800 Series Integrated Services
Routers - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5853/index.html)
(http://www.cisco.com/en/US/products/ps5853/index.html)  
http://cisco.com/go/2800 =\> [Cisco 2800 Series Integrated Services
Routers - Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps5854/index.html)
(http://www.cisco.com/en/US/products/ps5854/index.html)  
http://cisco.com/go/4900 =\> [Cisco Catalyst 4900 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6021/index.html)
(http://www.cisco.com/en/US/products/ps6021/index.html)  
http://cisco.com/go/vc10 =\> [VoiceCon 2010 - Cisco Events - Cisco
Systems](http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)(http://www.cisco.com/web/learning/le21/le34/voicecon/2010/index.html)  
http://cisco.com/go/tv10 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/1520 =\> [Cisco Aironet 1520 Series - Products &
Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps8368/index.html)
(http://www.cisco.com/en/US/products/ps8368/index.html)  
http://cisco.com/go/3750 =\> [Cisco Catalyst 3750 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/switches/ps5023/index.html)
(http://www.cisco.com/en/US/products/hw/switches/ps5023/index.html)  
http://cisco.com/go/2950 =\> [Cisco Catalyst 2950 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/switches/ps628/index.html)
(http://www.cisco.com/en/US/products/hw/switches/ps628/index.html)  
http://cisco.com/go/3560 =\> [Cisco Catalyst 3560 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/hw/switches/ps5528/index.html)
(http://www.cisco.com/en/US/products/hw/switches/ps5528/index.html)  
http://cisco.com/go/2960 =\> [Cisco Catalyst 2960 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6406/index.html)
(http://www.cisco.com/en/US/products/ps6406/index.html)  
http://cisco.com/go/cpi1 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio1 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME--CIO+Awarenett&CREATIVE=go/cio1)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME--CIO+Awarenett&CREATIVE;=go/cio1)  
http://cisco.com/go/tv11 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/7921 =\> [Cisco Unified Wireless IP Phone 7921G -
Cisco Systems](http://www.cisco.com/en/US/products/ps7071/index.html)
(http://www.cisco.com/en/US/products/ps7071/index.html)  
http://cisco.com/go/7931 =\> [Cisco Unified IP Phone 7931G - Cisco
Systems](http://www.cisco.com/en/US/products/ps7062/index.html)
(http://www.cisco.com/en/US/products/ps7062/index.html)  
http://cisco.com/go/1861 =\> [Cisco 1861 Integrated Services Router -
Cisco Systems](http://www.cisco.com/en/US/products/ps8321/index.html)
(http://www.cisco.com/en/US/products/ps8321/index.html)  
http://cisco.com/go/cpi2 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio2 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio2)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio2)  
http://cisco.com/go/tv12 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/cpi3 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio3 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio3)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio3)  
http://cisco.com/go/tv13 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/cpi4 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio4 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio4)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio4)  
http://cisco.com/go/tv14 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/9124 =\> [Cisco MDS 9124 Multilayer Fabric Switch -
Cisco Systems](http://www.cisco.com/en/US/products/ps7079/index.html)
(http://www.cisco.com/en/US/products/ps7079/index.html)  
http://cisco.com/go/cpi5 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio5 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio5)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio5)  
http://cisco.com/go/nw05 =\> [Cisco Systems - Redirect to
Networkers](http://www.cisco.com/offer/nwol04/128101_1)
(http://www.cisco.com/offer/nwol04/128101\_1)  
http://cisco.com/go/tv15 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/2955 =\> [Cisco Catalyst 2955 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps6738/index.html)
(http://www.cisco.com/en/US/products/ps6738/index.html)  
http://cisco.com/go/2975 =\> [Cisco Catalyst 2975 Series Switches -
Products & Services - Cisco
Systems](http://www.cisco.com/en/US/products/ps10081/index.html)
(http://www.cisco.com/en/US/products/ps10081/index.html)  
http://cisco.com/go/cpi6 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio6 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio6)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio6)  
http://cisco.com/go/cgv6 =\> [Cisco Carrier-Grade IPv6 Solution - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns1017/networking_solutions_solution_category.html)
(http://www.cisco.com/en/US/netsol/ns1017/networking\_solutions\_solution\_category.html)  
http://cisco.com/go/nw06 =\> [Cisco Systems - Redirect to
Networkers](http://www.cisco.com/offer/nwcdcpktads/133543_4)
(http://www.cisco.com/offer/nwcdcpktads/133543\_4)  
http://cisco.com/go/tv16 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/cpi7 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)  
http://cisco.com/go/cio7 =\> [Preparing Business for the Upturn with IT 
[Products & Services] - Cisco
Systems](http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep_business_for_upturn_generic.html?POSITION=PrintVanity&COUNTRY_SITE=us&CAMPAIGN=EMME%2D%2DCIO+Awarenett&CREATIVE=go/cio7)
(http://www.cisco.com/en/US/solutions/ns340/ns856/ns870/prep\_business\_for\_upturn\_generic.html?POSITION=PrintVanity&COUNTRY;\_SITE=us&CAMPAIGN;=EMME%2D%2DCIO+Awarenett&CREATIVE;=go/cio7)  
http://cisco.com/go/tv17 =\> [Telepresence - Overview - Cisco
Systems](http://www.cisco.com/en/US/netsol/ns669/networking_solutions_solution_segment_home.html)
(http://www.cisco.com/en/US/netsol/ns669/networking\_solutions\_solution\_segment\_home.html)  
http://cisco.com/go/cpi8 =\> [Cisco.com Login
Page](http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
(http://www.cisco.com/en/US/partner/partners/pr47/newsletter/us.shtml)
