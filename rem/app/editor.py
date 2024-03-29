from textual import on
from textual.binding import Binding
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Header, Footer, TextArea
from textual.app import ComposeResult # type: ignore

from ..qplcomp import prepare_env

from ..qrefine import mls



class Editor(Screen):

    BINDINGS = [
        Binding("ctrl+j", "play_backward", "◀◀", priority=True),
        Binding("ctrl+o", "step_backward", "◀", priority=True),
        Binding("ctrl+p", "step_forward", "▶", priority=True),
        Binding("ctrl+l", "play_forward", "▶▶", priority=True),
    ]

    def action_step_forward(self) -> bool:
        res = self.mls.step_forward(self.code_area.text)

        if res is not None:
            self.code_area.text = res

        self.mls_info.text = self.mls.info
        self.goal_area.text = self.mls.prover_info
        self.verified_area.text = self.mls.verified_code

        # verified_area scroll to end
        self.verified_area.scroll_end(animate = False)

        # set the cursor to the end
        self.verified_area.select_all()
        self.verified_area.move_cursor(self.verified_area.cursor_location)

        return res is not None


    def action_step_backward(self) -> bool:
        res = self.mls.step_backward()

        if res is not None:
            self.code_area.text = res + self.code_area.text


        self.mls_info.text = self.mls.info
        self.goal_area.text = self.mls.prover_info
        self.verified_area.text = self.mls.verified_code

        # verified_area scroll to end
        self.verified_area.scroll_end(animate = False)

        # set the verified_area cursor to the end
        self.verified_area.select_all()
        self.verified_area.move_cursor(self.verified_area.cursor_location)

        # push the code_area cursor backwards
        if res is not None:
            row_offset = res.count('\n')
            col_offset = len(res.split('\n')[-1])
            self.code_area.move_cursor_relative(row_offset, col_offset)

        return res is not None

    def action_play_forward(self) -> None:
        while self.action_step_forward():
            pass

    def action_play_backward(self) -> None:
        while self.action_step_backward():
            pass

    def compose(self) -> ComposeResult:

        self.verified_area = TextArea(
            "",
            id='verified-area',
            show_line_numbers=True,
            read_only=True
        )
        self.code_area = TextArea(
            "// put your code here ...", 
            id='code-area',
            show_line_numbers=True,
            tab_behavior='indent'
        )

        self.goal_area = TextArea(read_only=True)

        self.mls_info = TextArea(read_only=True)

        self.mls = mls.MLS(prepare_env())

        yield Header()

        yield Horizontal(
            Vertical(
                self.verified_area,
                self.code_area,
            ),
            Vertical(
                self.goal_area,
                self.mls_info,
            ),
                
        )

        yield Footer()

    @on(TextArea.SelectionChanged)
    def show_frame(self, event: TextArea.SelectionChanged) -> None:
        if event.text_area.id == 'verified-area':
            
            # avoid the empty selection
            if self.verified_area.text == "":
                return
            
            # calculate the pos of the cursor 
            pos = len(self.verified_area.get_text_range((0,0), event.selection.end)) + 1
            
            self.mls.set_cursor(pos)

            self.mls_info.text = self.mls.info
            self.goal_area.text = self.mls.prover_info
            
    