import plotly.graph_objs as go


def create_skill_chart(skill, proficiency, description, icon):
    fig = go.Figure(go.Pie(
        values=[proficiency, 100 - proficiency],
        labels=[f"({proficiency}%)", ""],
        hole=0.6,
        textinfo='label',
        hoverinfo='none'
    ))
    fig.update_traces(marker=dict(colors=['blue', 'white']))
    #fig.update_layout(title=f"{skill}", title_font={'size': 24}, showlegend=False)
    #experimental
    # Adding a title in the middle of the donut chart
    fig.add_annotation(
        go.layout.Annotation(
            text=f"<b>{skill}</b>",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(size=24),
            align='center',
            valign='middle'
        )
    )
    fig.update_layout(showlegend=False)
    return fig, description