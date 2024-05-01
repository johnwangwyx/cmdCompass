import customtkinter as ctk

class CollectionOperation(ctk.CTkFrame):
    def __init__(self, master, collections, on_collection_select, on_add_collection_click, **kwargs):
        super().__init__(master, **kwargs)

        self.collections = collections
        self.on_collection_select = on_collection_select
        self.on_add_collection_click = on_add_collection_click

        # Collection dropdown
        self.collection_dropdown = ctk.CTkOptionMenu(
            self,
            values=[collection.name for collection in self.collections],
            command=self.on_collection_select
        )
        self.collection_dropdown.pack(side=ctk.LEFT, padx=(10, 0), pady=10)

        # Add new collection button
        self.add_collection_button = ctk.CTkButton(
            self,
            text="+",
            width=40,
            height=40,
            command=self.on_add_collection_click
        )
        self.add_collection_button.pack(side=ctk.LEFT, padx=(5, 10), pady=10)