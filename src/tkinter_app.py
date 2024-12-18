from tkinter import Tk, Label, Button, Text, END, Scrollbar, ttk, WORD, StringVar, W, E, N, S
import pyperclip
from dotenv import load_dotenv

from config.providers import PROVIDERS
from config.prompts import PROMPTS
from config.tones import TONES
from services.text_rewriter import rewrite_text

# Load environment variables
load_dotenv()

class FloatingRewriter(Tk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Text Rewriter")
        self.attributes('-topmost', True)
        self.resizable(True, True)
        self.configure(bg='#1e1e1e')  # Darker background
        self.geometry('1400x800')  # Increased window size

        # Define colors for dark theme
        self.COLORS = {
            'bg_dark': '#1e1e1e',      # Main background
            'bg_medium': '#2d2d2d',     # Secondary background
            'bg_light': '#363636',      # Lighter background for hover
            'fg_main': '#ffffff',       # Main text color
            'fg_dim': '#cccccc',        # Dimmed text color
            'accent': '#007acc',        # Accent color (VS Code blue)
            'hover': '#404040',         # Hover state
            'active': '#505050',        # Active/pressed state
            'border': '#404040'         # Border color
        }

        self._setup_styles()
        self._create_layout()
        self._setup_bindings()

    def _setup_styles(self):
        """Setup dark theme styles"""
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        # Configure base style
        self.style.configure('.',
            background=self.COLORS['bg_dark'],
            foreground=self.COLORS['fg_main'],
            fieldbackground=self.COLORS['bg_medium'],
            selectbackground=self.COLORS['accent'],
            selectforeground=self.COLORS['fg_main']
        )
        
        # Frame style
        self.style.configure('TFrame', background=self.COLORS['bg_dark'])
        
        # Button style
        self.style.configure('Dark.TButton',
            background=self.COLORS['bg_light'],
            foreground=self.COLORS['fg_main'],
            padding=(20, 15),
            relief='flat',
            font=('Segoe UI', 12)
        )
        self.style.map('Dark.TButton',
            background=[('pressed', self.COLORS['active']), 
                       ('active', self.COLORS['hover'])],
            foreground=[('pressed', self.COLORS['fg_dim']), 
                       ('active', self.COLORS['fg_main'])]
        )
        
        # Label style
        self.style.configure('Dark.TLabel',
            background=self.COLORS['bg_dark'],
            foreground=self.COLORS['fg_main'],
            padding=(5, 2),
            font=('Segoe UI', 12)
        )
        
        # Combobox style
        self.style.configure('Dark.TCombobox',
            background=self.COLORS['bg_medium'],
            fieldbackground=self.COLORS['bg_medium'],
            foreground=self.COLORS['fg_main'],
            arrowcolor=self.COLORS['fg_main'],
            selectbackground=self.COLORS['accent'],
            selectforeground=self.COLORS['fg_main'],
            padding=(10, 8),
            font=('Segoe UI', 12)
        )
        self.style.map('Dark.TCombobox',
            fieldbackground=[('readonly', self.COLORS['bg_medium'])],
            selectbackground=[('readonly', self.COLORS['accent'])],
            selectforeground=[('readonly', self.COLORS['fg_main'])],
            background=[('readonly', self.COLORS['bg_medium'])],
            foreground=[('readonly', self.COLORS['fg_main'])]
        )

    def _create_layout(self):
        """Create the main layout"""
        # Create main frame
        self.main_frame = ttk.Frame(self, padding="20", style='TFrame')
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=1)

        self._create_text_area()
        self._create_controls()

    def _create_text_area(self):
        """Create the text area section"""
        left_frame = ttk.Frame(self.main_frame, style='TFrame')
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)

        self.text_area = Text(left_frame, 
            width=60, 
            height=10, 
            wrap=WORD, 
            font=('Segoe UI', 18),
            bg=self.COLORS['bg_medium'],
            fg=self.COLORS['fg_main'],
            insertbackground=self.COLORS['accent'],
            selectbackground=self.COLORS['accent'],
            selectforeground=self.COLORS['fg_main'],
            relief='flat',
            borderwidth=0,
            padx=20,
            pady=20
        )
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.text_area.configure(
            highlightthickness=1,
            highlightbackground=self.COLORS['border'],
            highlightcolor=self.COLORS['accent']
        )

    def _create_controls(self):
        """Create the control panel"""
        right_frame = ttk.Frame(self.main_frame, style='TFrame')
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Provider selection
        ttk.Label(right_frame, text="Provider:", style='Dark.TLabel').grid(
            row=0, column=0, sticky="w", pady=(0, 8))
        self.provider_var = StringVar(value=list(PROVIDERS.keys())[0])
        self.provider_dropdown = ttk.Combobox(right_frame, textvariable=self.provider_var, 
            values=list(PROVIDERS.keys()), state='readonly', style='Dark.TCombobox',
            width=30)
        self.provider_dropdown.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        # Model selection
        ttk.Label(right_frame, text="Model:", style='Dark.TLabel').grid(
            row=2, column=0, sticky="w", pady=(0, 8))
        self.model_var = StringVar(value=PROVIDERS[self.provider_var.get()][0])
        self.model_dropdown = ttk.Combobox(right_frame, textvariable=self.model_var, 
            values=PROVIDERS[self.provider_var.get()], state='readonly', style='Dark.TCombobox',
            width=30)
        self.model_dropdown.grid(row=3, column=0, sticky="ew", pady=(0, 20))

        # Prompt selection
        ttk.Label(right_frame, text="Task:", style='Dark.TLabel').grid(
            row=4, column=0, sticky="w", pady=(0, 8))
        self.prompt_var = StringVar(value=list(PROMPTS.keys())[0])
        prompt_dropdown = ttk.Combobox(right_frame, textvariable=self.prompt_var,
            values=list(PROMPTS.keys()), state='readonly', style='Dark.TCombobox',
            width=30)
        prompt_dropdown.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        # Tone selection
        ttk.Label(right_frame, text="Tone:", style='Dark.TLabel').grid(
            row=6, column=0, sticky="w", pady=(0, 8))
        self.tone_var = StringVar(value=list(TONES.keys())[0])
        tone_dropdown = ttk.Combobox(right_frame, textvariable=self.tone_var,
            values=list(TONES.keys()), state='readonly', style='Dark.TCombobox',
            width=30)
        tone_dropdown.grid(row=7, column=0, sticky="ew", pady=(0, 20))

        # Buttons
        ttk.Button(right_frame, text="Get Clipboard", command=self.get_clipboard, 
            style='Dark.TButton').grid(row=8, column=0, sticky="ew", pady=(0, 15))
        ttk.Button(right_frame, text="Rewrite", command=self.rewrite, 
            style='Dark.TButton').grid(row=9, column=0, sticky="ew", pady=(0, 15))
        ttk.Button(right_frame, text="Copy", command=self.copy_text, 
            style='Dark.TButton').grid(row=10, column=0, sticky="ew", pady=(0, 15))

        # Status label
        self.status_var = StringVar(value="Ready")
        self.status_label = ttk.Label(right_frame, 
            textvariable=self.status_var, 
            style='Dark.TLabel', 
            wraplength=300,
            justify='center'
        )
        self.status_label.grid(row=11, column=0, sticky="ew", pady=(25, 0))

        # Title bar for dragging
        self.title_bar = ttk.Frame(right_frame, style='TFrame', height=4)
        self.title_bar.grid(row=12, column=0, sticky="ew", pady=(15, 0))

    def _setup_bindings(self):
        """Setup event bindings"""
        self.provider_dropdown.bind('<<ComboboxSelected>>', self.update_models)
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.on_move)

    def update_models(self, event=None):
        """Update the model list based on selected provider"""
        provider = self.provider_var.get()
        self.model_dropdown['values'] = PROVIDERS[provider]
        self.model_var.set(PROVIDERS[provider][0])

    def start_move(self, event):
        """Start window drag"""
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        """Handle window drag"""
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f'+{x}+{y}')

    def get_clipboard(self):
        """Get text from clipboard"""
        try:
            text = pyperclip.paste()
            self.text_area.delete('1.0', END)
            self.text_area.insert('1.0', text)
            self.status_var.set("Clipboard content loaded")
        except Exception as e:
            self.status_var.set(f"Error getting clipboard: {str(e)}")

    def rewrite(self):
        """Rewrite the text using selected provider"""
        text = self.text_area.get('1.0', END).strip()
        if not text:
            self.status_var.set("No text to rewrite")
            return

        try:
            provider = self.provider_var.get()
            model = self.model_var.get()
            self.status_var.set(f"Rewriting with {provider} - {model}...")
            self.update()

            rewritten = rewrite_text(
                text,
                provider,
                model,
                self.prompt_var.get(),
                self.tone_var.get(),
                PROMPTS,
                TONES
            )

            if rewritten:
                self.text_area.delete('1.0', END)
                self.text_area.insert('1.0', rewritten)
                self.status_var.set("Text rewritten")
            else:
                self.status_var.set("Error during rewriting")

        except Exception as e:
            self.status_var.set(f"Error: {str(e)}")

    def copy_text(self):
        """Copy text to clipboard"""
        text = self.text_area.get('1.0', END).strip()
        if text:
            pyperclip.copy(text)
            self.status_var.set("Text copied to clipboard")
        else:
            self.status_var.set("No text to copy")

def main():
    app = FloatingRewriter()
    app.mainloop()

if __name__ == "__main__":
    main()
