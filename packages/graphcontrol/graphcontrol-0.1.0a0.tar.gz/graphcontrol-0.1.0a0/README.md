# GraphControl

A project to control Hugging Face Spaces, datasets, and models as directed acyclic graphs.

> [!CAUTION]
> GraphControl is under active development.

> [!NOTE]
> GraphControl is a portfolio project and not accepting contributions at this time. Thank you for your interest!

## Concept

The concept of GraphControl is simple – control compute enabled nodes of a DAG. However, this is more difficult in
practice, especially when the nodes exist on a remote network or require interacting with inference APIs. Regardless, 
the intent is to enable engineers with a root node (Controller) that manages several interfaces:

<ol>
    <li>compute nodes (SpaceNodes)</li>
    <li>data nodes (DatasetNodes)</li>
    <li>model nodes (TransformerNodes, and DiffuserNodes)</li>
</ol>

The control node is aware of each child node's capabilities, and as such – may not qualify as a router seen in other DAG 
centered libraries like LangGraph.

## Usage

> [!CAUTION]
> GraphControl is under active development.

GraphControl is not ready for use. Do not install the library with any expectation that it works. Rather, it is recommended
to [watch](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#configuring-your-watch-settings-for-an-individual-repository)
the repo.