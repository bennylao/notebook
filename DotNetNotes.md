# Dot Net MAUI
.NET MAUI is a multi-platform framework for creating native desktop and mobile apps with C# and XAML. .NET MAUI is an acronym for Multi-platform Application User Interface. Using .NET MAUI, you can design mobile apps that can run on Windows, Android, iOS, iPadOS, and macOS.

## Fundamentals
Reference: [Create a cross-platform app with .NET MAUI](https://learn.microsoft.com/en-gb/training/modules/build-mobile-and-desktop-apps/)

### NuGet
NuGet is the package manager of third-party libraries in .NET applications.

### Technology Stack
![DotNetMAUIStack](docs/assets/dotNetMAUIStack.png)

### Project Structure
A .NET MAUI project initially contains:

In short: 
- The **MauiProgram.cs** file that contains the code for creating and configuring the Application object.    
- The **App.xaml** and **App.xaml.cs** files that provide UI resources and create the initial window for the application.
- The **AppShell.xaml** and **AppShell.xaml.cs** files that specify the initial page for the application and handle the registration of pages for navigation routing.
- The **MainPage.xaml** and **MainPage.xaml.cs** files that define the layout and UI logic for the page displayed by default in the initial window.

More details:
- **App.xaml**. This file defines the application resources that the app will use in the XAML layout.
- **App.xaml.cs**. This is the code-behind for the App.xaml file. This file defines the App class. This class represents your application at runtime. The constructor in this class creates an initial window and assigns it to the `MainPage` property; this property determines which page is displayed when the application starts running. Additionally, this class enables you to override common platform-neutral application lifecycle event handlers. Events include `OnStart`, `OnResume`, and `OnSleep`. These handlers are defined as members of the `Application` base class.
- **AppShell.xaml**. This file is a .NET MAUI application's main structure. The .NET MAUI `Shell` provides many features that are beneficial for multiple-platform apps including app styling, URI based navigation, and layout options including flyout navigation and tabs for the application's root.

#### Application 
- The `App` class constructor will, in turn, usually create an instance of the `AppShell` class and assign it to the `MainPage` property. It's this code that controls the first screen the user sees through what's defined in the `AppShell`.

The App class also contains:

- Methods for handling lifecycle events, including when the app is sent to the background (that is, when it ceases to be the foreground app).
    
- Methods for creating new `Windows` for the application. The .NET MAUI application has a single window by default, but you can create and launch additional windows, which is helpful in desktop and tablet applications.

#### Shell
.NET Multi-platform App UI (.NET MAUI) Shell reduces the complexity of app development by providing the fundamental features that most apps require, including:

- A single place to describe the visual hierarchy of an app.
- A common navigation user experience.
- A URI-based navigation scheme that permits navigation to any page in the app.
- An integrated search handler.

In a .NET MAUI Shell app, the app's visual hierarchy is described in a class that subclasses the Shell class. This class can consist of three main hierarchical objects:

- `FlyoutItem` or `TabBar`. A `FlyoutItem` represents one or more items in the flyout, and should be used when the navigation pattern for the app requires a flyout. A `TabBar` represents the bottom tab bar, and should be used when the navigation pattern for the app begins with bottom tabs and doesn't require a flyout.
- `Tab`, which represents grouped content, navigable by bottom tabs.
- `ShellContent`, which represents the ContentPage objects for each tab.

These objects don't represent any user interface, but rather the organization of the app's visual hierarchy. Shell takes these objects and produces the navigation user interface for the content.

#### Pages
Pages are the root of the UI hierarchy in .NET MAUI inside of a `Shell`. The default class `MainPage` derives from `ContentPage`, which is the simplest and most common page type. A content page simply displays its contents. .NET MAUI has several other built-in page types, too, including the following:

- `TabbedPage`: This is the root page used for tab navigation. A tabbed page contains child page objects; one for each tab.
    
- `FlyoutPage`: This page enables you to implement a master/detail style presentation. A flyout page contains a list of items. When you select an item, a view displaying the details for that item appears.

Other page types are available, and are mostly used for enabling different navigation patterns in multi-screen apps.

#### Views
A content page typically displays a view. A view enables you to retrieve and present data in a specific manner. The default view for a content page is a `ContentView`, which displays items as-is. Views can be considered as individual UI components (e.g., `Button`, `Label`, `Entry`(Text box)). 

## C# Notes

### Basics
Comment
```cs
// This is a csharp comment
```

Console print
```cs
// Console print without newline
Console.Write("Hello World!");
// Console print with newline at the end
Console.WriteLine("Hello World!");
```





