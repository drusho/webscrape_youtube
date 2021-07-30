# collapse
# List of Video Channels
yt_chan_jn = (
    df.groupby(["Channel Join Date", "Channel Name", "Channel Views (M)"])[
        "Subscribers (M)"
    ]
    .max()
    .to_frame()
    .reset_index()
)

# rename columns to increase readability
yt_chan_jn.rename(
    columns={
        "Channel Name": "Channel",
        "Channel Join Date": "Join Date",
        "Subscribers (M)": "Subscribers",
        "Channel Views (M)": "Channel Views",
    },
    inplace=True,
)

yt_chan_jn
# # style dateframe to highlight highest values
yt_chan_jn.style.format(
    formatter={"Subscribers": "{:,} M", "Channel Views": "{:,} M"}
).background_gradient(
    subset=["Channel Views", "Subscribers"], cmap="Wistia"
).set_caption(
    "Youtube Channels Ordered by Join Date"
).set_table_styles(
    [dict(selector="caption", props=[("text-align", "center"), ("font-size", "125%")])]
).hide_index()
