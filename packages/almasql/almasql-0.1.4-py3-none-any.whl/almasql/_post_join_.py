import typing


Unset = ...


async def post_join[LI: object, RI: object, K: typing.Any](
    _attribute_: str,
    _from_: typing.Callable[[set[K]], typing.Coroutine[typing.Any, typing.Any, typing.Iterable[RI]]],
    _where_: typing.Callable[[RI], K],
    _equal_: typing.Callable[[LI], K],
    _source_: list[LI],
    /,
    many = False,
    default = Unset,
) -> None:
    """
    Joins list of subrecords from function to list of record by `_attribute_`.
    Group subrecords if many is True.
    Excludes record from `source` if subrecord not found and `default` is unset.

    ```python
    class Author:
        id: UUID
        full_name: str

    class Book:
        id: UUID
        name: str
        author_id: UUID

    async def get_authors(
        ids: set[UUID],
    ) -> list[Author]:
        '''Returns list of authors'''

    books = [<list of books>]
    await post_join(
        'authors',
        get_authors,
        lambda author: author.id,
        lambda book: book.author_id,
        books,
    )
    for b in books:
        list_of_authors = ', '.join([author.full_name for author in b.authors])
        print(f'book {b.name} published by {list_of_authors}')
    ```
    """
    source_map = {_equal_(i): i for i in _source_}
    target_pks = set(source_map.keys())
    target_map = {_where_(i): i for i in await _from_(target_pks)}
    for target_pk, source_item in source_map.items():
        target_item = target_map.get(target_pk)
        if target_item is None:
            if default is Unset:
                _source_.remove(source_item)
            else:
                setattr(source_item, _attribute_, default)
            continue

        if not many:
            setattr(source_item, _attribute_, target_item)
            continue

        nested_items = getattr(source_item, _attribute_, None)
        if nested_items is None:
            nested_items = list()
            setattr(source_item, _attribute_, nested_items)
        nested_items.append(target_item)
