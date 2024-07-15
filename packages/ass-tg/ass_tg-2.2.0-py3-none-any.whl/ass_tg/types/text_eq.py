from ass_tg.entities import ArgEntities
from ass_tg.exceptions import ArgTypeError
from ass_tg.types.text import TextArg


class EqualsArg(TextArg):
    def __init__(self, equals: str, *args, **kwargs):
        self.equals = equals
        super().__init__(*args, **kwargs)

    def parse(self, text: str, offset: int, entities: ArgEntities) -> tuple[int, str]:

        if not text.startswith(self.equals):
            # raise ArgTypeError(_("Should contain {}!").format(Code(self.equals)))
            raise ArgTypeError(
                needed_type=self.needed_type,
                description=self.description,
                offset=offset,
                length=self.get_end(text, entities),
                text=text,
                examples=self.examples or {},
            )

        return super().parse(self.equals, offset, entities)

    @property
    def examples(self) -> dict[str, None]:
        return {
            self.equals: None
        }