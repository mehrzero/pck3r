#include <stdio.h>
#include <stdlib.h>
#include <sys/unistd.h>
#include <vte/vte.h>
#include <gtk/gtk.h>


/*
 *
 * this is c/gtk terminal emulator
 * i customize this for pck3r project and you can run this terminal
 * this terminal is an simple terminal and easy to use when you run pck3r
 * you can run this program by this command :
 *      $ pck3r term
 *
 */

static void child_ready(VteTerminal *terminal, GPid pid, GError *error, gpointer user_data)
{
    if (!terminal) return;
    if (pid == -1) gtk_main_quit();
}

/* go to home */
static void exec_x_home(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");

  char xhome[1000] ="xdg-open ";
  strcat(xhome, homeAdrs);

  system(xhome);

}
/* go to Downloads */
static void exec_x_downloads(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xdownloads[1000] ="xdg-open ";
  strcat(xdownloads, homeAdrs);
  strcat(xdownloads, "/Downloads");

  system(xdownloads);

}
/* go to Documents */
static void exec_x_documents(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xdocs[1000] ="xdg-open ";
  strcat(xdocs, homeAdrs);
  strcat(xdocs, "/Documents");

  system(xdocs);

}

/* go to Desktop */
static void exec_x_desktop(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xdesktop[1000] ="xdg-open ";
  strcat(xdesktop, homeAdrs);
  strcat(xdesktop, "/Desktop");

  system(xdesktop);

}

/* go to Pictures */
static void exec_x_pictures(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xpics[1000] ="xdg-open ";
  strcat(xpics, homeAdrs);
  strcat(xpics, "/Pictures");

  system(xpics);

}
/* go to Vidoes */
static void exec_x_vd(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xvd[1000] ="xdg-open ";
  strcat(xvd, homeAdrs);
  strcat(xvd, "/Videos");

  system(xvd);

}

/* go to Public */
static void exec_x_public(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xpubs[1000] ="xdg-open ";
  strcat(xpubs, homeAdrs);
  strcat(xpubs, "/Public");

  system(xpubs);

}
/* go to Templates */
static void exec_x_templates(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xtmp[1000] ="xdg-open ";
  strcat(xtmp, homeAdrs);
  strcat(xtmp, "/Templates");

  system(xtmp);

}
/* go to music */
static void exec_x_music(GtkWidget *wid, GtkWidget *win){

  char *homeAdrs = getenv("HOME");
  char xmus[1000] ="xdg-open ";
  strcat(xmus, homeAdrs);
  strcat(xmus, "/Music");

  system(xmus);

}

int main(int argc, char *argv[])
{
    /* pointer to HOME directory */

    char *home = getenv("HOME");

    /* icon path  */

    char path[1000] = {"\0"};
    strcat(path, home);
    strcat(path, "/.pck3r-GUI/pck3r-logo.png");

    /* create all widget */

    GtkWidget *win,
    *terminal,
    *first_box_terminal,
    *second_box_terminal,
    *open_home_directory,
    *open_downloads_directory,
    *open_desktop_directory,
    *open_pictures_directory,
    *open_public_directory,
    *open_templates_directory,
    *open_music_directory,
    *open_documents_directory,
    *open_videos_directory;


    /* Initialise GTK, the window and the terminal */
    gtk_init(&argc, &argv);
    terminal = vte_terminal_new();
    win = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(win), "pck3r-terminal-emulator");

    /* icon cpy to ~/.pck3r-GUI */


    /*Mehr ziro logo */
    gtk_window_set_icon_from_file(GTK_WINDOW(win), path,NULL);

    /* go to all standard directories GUI  */
    open_downloads_directory = gtk_button_new_with_label("go to downloads ");

    open_documents_directory = gtk_button_new_with_label("go to documents ");

    open_desktop_directory = gtk_button_new_with_label("go to desktop ");

    open_pictures_directory = gtk_button_new_with_label("go to pictures ");

    open_public_directory = gtk_button_new_with_label("go to public ");

    open_templates_directory = gtk_button_new_with_label("go to templates ");

    open_videos_directory = gtk_button_new_with_label("go to videos ");

    open_home_directory = gtk_button_new_with_label("go to home ");

    open_music_directory = gtk_button_new_with_label("go to music ");

    /* main boxes of terminal  */

    first_box_terminal = gtk_hbox_new(FALSE, 0);
    second_box_terminal = gtk_vbox_new(TRUE, 0);


    /* Start a new shell */
    gchar **envp = g_get_environ();
    gchar **command = (gchar *[]){g_strdup(g_environ_getenv(envp, "SHELL")), NULL };
    g_strfreev(envp);
    vte_terminal_spawn_async(VTE_TERMINAL(terminal),
        VTE_PTY_DEFAULT,
        home,         /* working directory  */
        command,      /* command */
        NULL,         /* environment */
        0,            /* spawn flags */
        NULL, NULL,   /* child setup */
        NULL,         /* child pid */
        -1,           /* timeout */
        NULL,         /* cancellable */
        child_ready,  /* callback */
        NULL);        /* user_data */



    /* Connect some signals */

    g_signal_connect(win, "delete-event", gtk_main_quit, NULL);

    g_signal_connect(terminal, "child-exited", gtk_main_quit, NULL);

    g_signal_connect(G_OBJECT(open_home_directory),
                    "clicked",
                    G_CALLBACK(exec_x_home),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_downloads_directory),
                    "clicked",
                    G_CALLBACK(exec_x_downloads),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_documents_directory),
                    "clicked",
                    G_CALLBACK(exec_x_documents),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_desktop_directory),
                    "clicked",
                    G_CALLBACK(exec_x_desktop),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_pictures_directory),
                    "clicked",
                    G_CALLBACK(exec_x_pictures),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_public_directory),
                    "clicked",
                    G_CALLBACK(exec_x_public),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_templates_directory),
                    "clicked",
                    G_CALLBACK(exec_x_templates),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_videos_directory),
                    "clicked",
                    G_CALLBACK(exec_x_vd),
                    (gpointer)win
                  );

    g_signal_connect(G_OBJECT(open_music_directory),
                    "clicked",
                    G_CALLBACK(exec_x_music),
                    (gpointer)win
                  );
   /*
    * combine two box (first_box_terminal and second_box_terminal)
    */

    gtk_box_pack_end(GTK_BOX(first_box_terminal), second_box_terminal, FALSE, FALSE, 0 );

    /*
     * add  terminal frame
     */
    gtk_box_pack_start(GTK_BOX(first_box_terminal), terminal, TRUE, TRUE, 0 );

    /*
     * add btn Desktop directory (GUI)
     */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_desktop_directory, FALSE, FALSE, 4);

    /*
     * add btn Documents directory (GUI)
     */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_documents_directory, FALSE, FALSE, 4);

    /*
    * add btn Downloads directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_downloads_directory, FALSE, FALSE, 4);


    /*
    * add btn Pictures directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_pictures_directory, FALSE, FALSE, 4);

    /*
    * add btn Public directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_public_directory, FALSE, FALSE, 4);

    /*
    * add btn Templates directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_templates_directory, FALSE, FALSE, 4);

    /*
    * add btn Music directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_music_directory, FALSE, FALSE, 4);

    /*
    * add btn Vidoes directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_videos_directory, FALSE, FALSE, 4);

    /*
    * add btn HOME directory (GUI)
    */
    gtk_box_pack_end(GTK_BOX(second_box_terminal), open_home_directory, FALSE, FALSE, 4);


    /*
     * maximize pck3r terminal
     * you can comment this section
     * if you dont want to maximize your pck3r terminal
     * and you can modify size or ...
     *  NEXT STEP : Put widgets together and run the main loop
     */

    gtk_window_maximize(win);
    gtk_container_add(GTK_CONTAINER(win), first_box_terminal);

    /*
     * render all
     */
    gtk_widget_show_all(win);
    system("clear");
    system("clear");
    gtk_main();
    system("clear");

}
