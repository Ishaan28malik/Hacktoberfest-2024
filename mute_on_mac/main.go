package main

import (
	"fmt"
	"log"
	"os/exec"

	"fyne.io/fyne/app"
	"fyne.io/fyne/widget"
)

func main() {
	var mute, unmute *widget.Button

	changeInput := func(f int) error {
		cmd := fmt.Sprintf(`set volume input volume %d`, f)
		return exec.Command("osascript", "-e", cmd).Run()
	}

	mute = widget.NewButton("   MUTE   ", func() {
		mute.Hide()
		unmute.Show()
		if err := changeInput(0); err != nil {
			log.Printf("mute failed: %s", err)
		}
	})

	unmute = widget.NewButton("UNMUTE", func() {
		unmute.Hide()
		mute.Show()
		if err := changeInput(100); err != nil {
			log.Printf("unmute failed: %s", err)
		}
	})

	unmute.Hide()

	w := app.New().NewWindow("Mac Mute")
	w.SetFixedSize(true)
	w.SetContent(widget.NewVBox(unmute, mute))
	w.ShowAndRun()
}
