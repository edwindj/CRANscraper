# -*- coding: utf-8 -*-

from json import load
from pattern.vector import Document, Model,L2

packages = load(file("packages.json"))

docs = [Document(p['description'], name=p['name']) for p in packages]
model = Model(docs)

lsa = model.reduce(L2)