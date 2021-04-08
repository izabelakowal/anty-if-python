from anty_if_course_code_python.gilded_rose import Item, GildedRose
def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"


def test_report():
    report_lines = []

    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 2

    for day in range(days):
        report_lines.append("-------- day %s --------" % day)
        report_lines.append("name, sellIn, quality")
        for item in items:
            report_lines.append(item)
        report_lines.append("")
        GildedRose(items).update_quality()

    assert [
        "'-------- day 0 --------'",
        "'name, sellIn, quality'",
        "+5 Dexterity Vest, 8, 18",
        "Aged Brie, 0, 2",
        "Elixir of the Mongoose, 3, 5",
        "Sulfuras, Hand of Ragnaros, 0, 80",
        "Sulfuras, Hand of Ragnaros, -1, 80",
        "Backstage passes to a TAFKAL80ETC concert, 13, 22",
        "Backstage passes to a TAFKAL80ETC concert, 8, 50",
        "Backstage passes to a TAFKAL80ETC concert, 3, 50",
        "Conjured Mana Cake, 1, 4",
        "''",
        "'-------- day 1 --------'",
        "'name, sellIn, quality'",
        "+5 Dexterity Vest, 8, 18",
        "Aged Brie, 0, 2",
        "Elixir of the Mongoose, 3, 5",
        "Sulfuras, Hand of Ragnaros, 0, 80",
        "Sulfuras, Hand of Ragnaros, -1, 80",
        "Backstage passes to a TAFKAL80ETC concert, 13, 22",
        "Backstage passes to a TAFKAL80ETC concert, 8, 50",
        "Backstage passes to a TAFKAL80ETC concert, 3, 50",
        "Conjured Mana Cake, 1, 4",
        "''",
    ] == [repr(item) for item in report_lines]


def assert_backstage_pass_quality(expected, sell_in, quality):
    items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)]
    GildedRose(items).update_quality()
    assert expected == items[0].quality


def test_backstage_pass():
    assert_backstage_pass_quality(22, 8, 20)
    assert_backstage_pass_quality(23, 4, 20)
    assert_backstage_pass_quality(23, 4, 20)
    assert_backstage_pass_quality(0, 0, 20)
    assert_backstage_pass_quality(23, 1, 20)
    assert_backstage_pass_quality(22, 6, 20)
    assert_backstage_pass_quality(23, 5, 20)
    assert_backstage_pass_quality(21, 11, 20)
    assert_backstage_pass_quality(22, 10, 20)


def assert_aged_brie_quality(expected, sell_in, quality):
    items = [Item("Aged Brie", sell_in, quality)]
    GildedRose(items).update_quality()
    assert expected == items[0].quality


def test_aged_brie():
    assert_aged_brie_quality(22, 0, 20)
    assert_aged_brie_quality(21, 1, 20)


def assert_generic_quality(expected, sell_in, quality):
    items = [Item("Something Generic", sell_in, quality)]
    GildedRose(items).update_quality()
    assert expected == items[0].quality


def test_generic():
    items = [Item("foo", -1, 3)]
    GildedRose(items).update_quality()
    assert 1 == items[0].quality
    assert_generic_quality(1, -1, 3)
    assert_generic_quality(1, 0, 3)
    assert_generic_quality(2, 1, 3)
    assert_generic_quality(0, 1, 0)
    assert_generic_quality(0, 1, 1)
