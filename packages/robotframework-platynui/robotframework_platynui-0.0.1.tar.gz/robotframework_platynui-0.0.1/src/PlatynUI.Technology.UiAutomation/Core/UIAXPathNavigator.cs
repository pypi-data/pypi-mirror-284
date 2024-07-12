﻿using System.Xml;
using System.Xml.XPath;
using PlatynUI.Technology.UiAutomation.Client;

namespace PlatynUI.Technology.UiAutomation.Core;

internal class UiaXPathNavigator : XPathNavigator
{
    private object? _current;
    private bool _findVirtual;
    private NameTable _nameTable = new();

    private IUIAutomationTreeWalker? _treeWalker;

    public UiaXPathNavigator(IUIAutomationElement? element = null, bool findVirtual = false)
    {
        element ??= Automation.RootElement;

        _findVirtual = findVirtual;

        _current = new AutomationElementNavigator(element, TreeWalker, findVirtual);

        _nameTable.Add(string.Empty);
    }

    protected UiaXPathNavigator(UiaXPathNavigator other)
    {
        if (other._current is AutomationElementNavigator navigator)
        {
            _current = navigator.Clone();
        }
        else if (other._current is AutomationPropertyNavigator propertyNavigator)
        {
            _current = propertyNavigator.Clone();
        }
        else
        {
            throw new NotSupportedException();
        }

        _nameTable = other._nameTable;
        _treeWalker = other._treeWalker;
        _findVirtual = other._findVirtual;
    }

    protected IUIAutomationTreeWalker TreeWalker => _treeWalker ??= Automation.RawViewWalker;

    public override string Value
    {
        get
        {
            switch (_current)
            {
                case AutomationPropertyNavigator navigator:
                {
                    var cp = navigator.Element;

                    if (cp == null)
                    {
                        return string.Empty;
                    }

                    var p = navigator.Current;

                    try
                    {
                        if (p.Id == -1)
                        {
                            if (p.Name == "Role")
                                return Automation.ControlTypeNameFromId(cp.CurrentControlType);

                            return string.Empty;
                        }
                        else if (p.Id == -2)
                        {
                            if (p.Name == "ProcessName")
                            {
                                try
                                {
                                    return System.Diagnostics.Process.GetProcessById(cp.CurrentProcessId).ProcessName;
                                }
                                catch
                                {
                                    // DO NOTHING
                                }
                            }

                            return string.Empty;
                        }

                        var v = cp.GetCurrentPropertyValueEx((int)p.Id, 0);

                        return Automation.ConvertPropertyValue(p.Name, v)?.ToString() ?? string.Empty;
                    }
                    catch
                    {
                        return string.Empty;
                    }
                }
                case AutomationElementNavigator _:
                    return string.Empty;
                default:
                    return string.Empty;
            }
        }
    }

    public override XmlNameTable NameTable => _nameTable;

    public override XPathNodeType NodeType
    {
        get
        {
            switch (_current)
            {
                case AutomationElementNavigator elementNavigator when elementNavigator.Current == null:
                    return XPathNodeType.All;
                case AutomationElementNavigator elementNavigator
                    when Automation.CompareElements(elementNavigator.Current, Automation.RootElement):
                    return XPathNodeType.Root;
                case AutomationElementNavigator _:
                    return XPathNodeType.Element;
                case AutomationPropertyNavigator _:
                    return XPathNodeType.Attribute;
                default:
                    return XPathNodeType.All;
            }
        }
    }

    public override string LocalName
    {
        get
        {
            switch (_current)
            {
                case AutomationElementNavigator navigator:
                    if (navigator.Current == null)
                    {
                        throw new NotSupportedException();
                    }

                    return Automation.ControlTypeNameFromId(navigator.Current.CurrentControlType);
                case AutomationPropertyNavigator navigator:
                    return navigator.Current.Name;
                default:
                    throw new NotSupportedException();
            }
        }
    }

    public override string Name => LocalName;

    public override string NamespaceURI => _nameTable.Get(string.Empty) ?? string.Empty;

    public override string Prefix => _nameTable.Get(string.Empty) ?? string.Empty;

    public override string BaseURI => string.Empty;

    public override bool IsEmptyElement => false;

    public override object? UnderlyingObject =>
        _current switch
        {
            AutomationElementNavigator navigator => navigator.Current,
            AutomationPropertyNavigator navigator => navigator.Current,
            _ => throw new NotSupportedException(),
        };

    public override string ToString()
    {
        var result = NodeType.ToString();
        switch (NodeType)
        {
            case XPathNodeType.Element:
                result += ", Name=\"" + Name + '"';
                break;
            case XPathNodeType.Attribute:
            case XPathNodeType.Namespace:
            case XPathNodeType.ProcessingInstruction:
                result += ", Name=\"" + Name + '"';
                result += ", Value=\"" + Value + '"';
                break;
            case XPathNodeType.Text:
            case XPathNodeType.Whitespace:
            case XPathNodeType.SignificantWhitespace:
            case XPathNodeType.Comment:
                result += ", Value=\"" + Value + '"';
                break;
        }

        return result;
    }

    public override XPathNavigator Clone()
    {
        return new UiaXPathNavigator(this);
    }

    public override bool MoveToAttribute(string localName, string namespaceURI)
    {
        return base.MoveToAttribute(localName, namespaceURI);
    }

    public override bool MoveToNext(XPathNodeType type)
    {
        return base.MoveToNext(type);
    }

    public override bool MoveToFirstAttribute()
    {
        switch (_current)
        {
            case AutomationElementNavigator current:
            {
                var n = new AutomationPropertyNavigator(current);
                if (!n.MoveToFirst())
                {
                    return false;
                }

                _current = n;

                return true;
            }
            default:
                return false;
        }
    }

    public override bool MoveToNextAttribute()
    {
        if (_current is AutomationPropertyNavigator current)
        {
            return current.MoveToNext();
        }

        return false;
    }

    public override bool MoveToFirstNamespace(XPathNamespaceScope namespaceScope)
    {
        throw new NotImplementedException();
    }

    public override bool MoveToNextNamespace(XPathNamespaceScope namespaceScope)
    {
        throw new NotImplementedException();
    }

    public override bool MoveToNext()
    {
        if (_current is AutomationElementNavigator current)
        {
            return current.MoveToNext();
        }

        return false;
    }

    public override bool MoveToPrevious()
    {
        if (_current is AutomationElementNavigator current)
        {
            return current.MoveToPrevious();
        }

        return false;
    }

    public override bool MoveToFirstChild()
    {
        if (_current is AutomationElementNavigator current)
        {
            current = new AutomationElementNavigator(current, TreeWalker, _findVirtual);
            if (current.MoveToFirst())
            {
                _current = current;
                return true;
            }
        }

        return false;
    }

    public override bool MoveToParent()
    {
        switch (_current)
        {
            case AutomationElementNavigator c when c.ParentNavigator != null:
                _current = c.ParentNavigator;
                return true;
            case AutomationElementNavigator c:
            {
                var v = TreeWalker.GetParentElement(c.Current);
                if (v == null)
                {
                    return false;
                }

                _current = new AutomationElementNavigator(v, TreeWalker, _findVirtual);
                return true;
            }
            case AutomationPropertyNavigator navigator:
                _current = navigator.Parent;
                break;
        }

        return false;
    }

    public override bool MoveTo(XPathNavigator other)
    {
        if (other is UiaXPathNavigator o)
        {
            if (o._current is AutomationElementNavigator navigator)
            {
                _current = navigator.Clone();
            }
            else if (o._current is AutomationPropertyNavigator propNavigator)
            {
                _current = propNavigator.Clone();
            }
            else
            {
                throw new NotSupportedException();
            }

            _nameTable = o._nameTable;
            _treeWalker = o._treeWalker;
            _findVirtual = o._findVirtual;

            return true;
        }

        return false;
    }

    public override bool MoveToId(string id)
    {
        return false;
    }

    public override bool IsSamePosition(XPathNavigator other)
    {
        return other switch
        {
            UiaXPathNavigator o
                when o._current is AutomationElementNavigator current && _current is AutomationElementNavigator current1
                => Automation.CompareElements(current.Parent, current1.Parent)
                    && current.CurrentIndex == current1.CurrentIndex
                    && Automation.CompareElements(current.Current, current1.Current),
            UiaXPathNavigator o => _current == o._current,
            _ => false,
        };
    }

    public override string GetAttribute(string localName, string namespaceURI)
    {
        return base.GetAttribute(localName, namespaceURI);
    }
}
